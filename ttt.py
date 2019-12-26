# coding: utf-8

#import qdarkstyle
import ftrack_api.accessor.disk
import ftrack_api.structure.origin
import ftrack_api.entity.location
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot,QObject,pyqtSignal
from pages import *
from child import *
import sys


hei = []
pro_id = []
project_dict = {}
seq_dict = {}


#登录注册
class MyClass(QDialog):
    def __init__(self):
        super(MyClass,self).__init__()
        self.initUI()

    def initUI(self):
        frame =QFrame(self)
        lbl1 = QLabel("域  名:",frame)
        lbl2 = QLabel('密  保', frame)
        lbl3 = QLabel('用户名:', frame)
        lbl2.move(0,30)
        lbl3.move(0,60)

        self.server_url = QLineEdit(frame)
        self.api_key = QLineEdit(frame)
        self.api_user = QLineEdit(frame)
        self.server_url.move(50,0)
        self.api_key.move(50, 30)
        self.api_user.move(50,60)
        self.api_key.setEchoMode(QLineEdit.Password)

        Login = QPushButton('登录',frame)
        Quit = QPushButton('退出',frame)
        Login.clicked.connect(self.mybut)
        Quit.clicked.connect(self.mybut)

        Login.move(0,90)
        Quit.move(80,90)
        frame.move(50,50)
        frame.resize(400,400)

    def mybut(self):
        source = self.sender()
        if source.text() == '登录':
            pass
        elif source.text() == '退出':
            QApplication.instance().exit()

        server_url = self.server_url.text()
        api_key = self.api_key.text()
        api_user = self.api_user.text()

        session = ftrack_api.Session(
            server_url=server_url,
            api_key=api_key,
            api_user=api_user
        )

        for i in sorted(session.types.keys()):
            print i
            if i == 'Appointment':
                print '登录成功'
                self.close()
                window.show()
                print "输入正确,跳转至主界面"
            else:
                return None


#主窗口
class MainWindow(QtWidgets.QMainWindow, Ui_Form):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUI()
        self.pushButton_2.clicked.connect(self.publish)
        self.pushButton.clicked.connect(self.browse)

    def initUI(self):
        self.setAcceptDrops(True)

    #拖拽路径去除前缀
    def dragEnterEvent(self, e):
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self,e):
        self.comboBox.addItem(e.mimeData().text()[8:])

    #关联子窗口
    def browse(self):
        child.show()

    #提交功能的按钮
    def publish(self):
        self.lineEdit.clear()

#自定义信号与槽，对应返回按钮
# class Signal(QObject):
#     #声明参数信号
#     sginal = pyqtSignal('Shot','Sequence','Project')
#     def __init__(self,parent = None):
#         super(Signal,self).__init__(parent)




#子窗口
class ChildWindow(QtWidgets.QDialog, Ui_Dialog):

    #子窗口的显示操作
    def __init__(self):
        super(ChildWindow,self).__init__()
        self.setupUi(self)
        projects = session.query('Project')
        tm = 0
        ti = 1
        projectlist = []
        for project in projects:
            st = str(project['name'])
            ne = QTableWidgetItem(st)
            self.textEteil1.setItem(tm,0,ne)
            ne = QTableWidgetItem('Project')
            self.textEteil1.setItem(tm, ti, ne)
            tm += 1
            projectlist.append(st)

        self.pushButton.clicked.connect(self.out)
        self.textEteil1.itemDoubleClicked.connect(self.getItem)
        self.pushButton2.clicked.connect(lambda: self.back('Shot'))

        self.pushButton1.clicked.connect(self.fix)

    #点击列表跳到下一级
    def getItem(self,item):
        self.textEteil.setPlaceholderText(str(item.text()))

        tm = 0
        ti = 1
        project_s = []
        try:
            #获取列表的item.text()来查找Project的项目
            projects_1 = session.query('Project where name is ' + str(item.text()))
            proid = projects_1[0]['id']
            pro_id.append(proid)
            hierarchy = projects_1[0]['children']
            hei.append(hierarchy)
            for a in hierarchy:
                project_s.append(a['name'])
            for x, v in enumerate(project_s):
                self.textEteil1.setRowCount(x + 1)
                ne = QTableWidgetItem(v)
                self.textEteil1.setItem(tm, 0, ne)
                type_p = hierarchy[x]
                types = type_p['object_type']
                se = str(types['name'])
                ne = QTableWidgetItem(se)
                project_dict[v] = se
                print project_dict
                self.textEteil1.setItem(tm, ti, ne)
                tm += 1
                #seq_dict.clear()
        except Exception:
                self.textEteil.setPlaceholderText(str(item.text()))
                tm = 0
                ti = 1
                try:
                    for k,v in project_dict.items():
                        print k,v
                        v = str(v)
                        v = v.replace(' ', '')
                        #判断列表获取的item.text()与字典project_dict中的k是否一样
                        if k == item.text():
                            seq1 = session.query(v + ' where name is '+str(item.text()))
                            sequid = seq1[0]['parent_id']
                            for i,a in enumerate(pro_id):
                                #判断自身的id与父id是否相等
                                if a == sequid:
                                    t = seq1[0]['children']
                                    for i, v in enumerate(t):
                                        self.textEteil1.setRowCount(i + 1)
                                        ne = QTableWidgetItem(v['name'])
                                        self.textEteil1.setItem(tm, 0, ne)
                                        type_p = t[i]
                                        print type_p
                                        types = type_p['object_type']
                                        se = str(types['name'])
                                        ne = QTableWidgetItem(se)
                                        seq_dict[v['name']] = se
                                        print seq_dict
                                        self.textEteil1.setItem(tm, ti, ne)
                                        tm += 1
                                else:
                                    #因为production和asset的地址在一个列表里，所以要分开
                                    #s[1]['children'],s[0]['children']
                                    if k == 'production':
                                        for s in hei:
                                            a = s[1]['children']
                                            for i, v in enumerate(a):
                                                self.textEteil1.setRowCount(i+1)
                                                ne = QTableWidgetItem(v['name'])
                                                self.textEteil1.setItem(tm, 0, ne)
                                                type_p = a[i]['object_type']['name']
                                                seq_dict[v['name']] = type_p
                                                print seq_dict
                                                ne = QTableWidgetItem(type_p)
                                                self.textEteil1.setItem(tm, ti, ne)
                                                tm += 1

                                    else:
                                        for s in hei:
                                            a = s[0]['children']
                                            for i, v in enumerate(a):
                                                self.textEteil1.setRowCount(i + 1)
                                                ne = QTableWidgetItem(v['name'])
                                                self.textEteil1.setItem(tm, 0, ne)
                                                type_p = a[i]['object_type']['name']
                                                seq_dict[v['name']] = type_p
                                                print seq_dict
                                                ne = QTableWidgetItem(type_p)
                                                self.textEteil1.setItem(tm, ti, ne)
                                                tm += 1

                        else:
                            self.textEteil.setPlaceholderText(str(item.text()))
                            tm = 0
                            ti = 1
                            for k,v in seq_dict.items():
                                print k,v
                                v = str(v)
                                s = v.replace(' ','')
                                if k == item.text():
                                    shot1 = session.query(v + ' where name is ' + str(item.text()))
                                    t = shot1[0]['children']
                                    for i, v in enumerate(t):
                                        self.textEteil1.setRowCount(i + 1)
                                        ne = QTableWidgetItem(v['name'])
                                        self.textEteil1.setItem(tm, 0, ne)
                                        type_p = t[i]
                                        types = type_p['object_type']
                                        se = str(types['name'])
                                        ne = QTableWidgetItem(se)
                                        self.textEteil1.setItem(tm, ti, ne)
                                        tm += 1

                except Exception:
                    pass
                    # tm = 0
                    # ti = 1
                    # for k, v in seq_dict.items():
                    #     #AssetBuild 中间是没有空格的 如果有空格会报错
                    #     print k, v
                    #     v = str(v)
                    #     s = v.replace(' ','')
                    #     print s
                    #     if k == item.text():
                    #         task1 = session.query(s + ' where name is ' + str(item.text()))
                    #         t = task1[0]['children']
                    #         print task1
                    #         for i, v in enumerate(t):
                    #             print i, v
                    #             self.textEteil1.setRowCount(i + 1)
                    #             ne = QTableWidgetItem(v['name'])
                    #             self.textEteil1.setItem(tm, 0, ne)
                    #             type_p = t[0]
                    #             types = type_p['object_type']
                    #             se = str(types['name'])
                    #             ne = QTableWidgetItem(se)
                    #             self.textEteil1.setItem(tm, ti, ne)
                    #             tm += 1

    #返回上一级

    def back(self,char):
        tm = 0
        ti = 1
        print project_dict
        print seq_dict
        for k, v in seq_dict.items():
            print k, v
            if v == char:
                #三次返回
                a = len([k for k, v in seq_dict.items()])
                self.textEteil1.setRowCount(a)
                for k,v in seq_dict.items():
                    print k,v
                    #if v == 'Shot' or v == 'Asset Build' or v == 'Task':
                    if v == 'Sequence':
                        ne = QTableWidgetItem(k)
                        self.textEteil1.setItem(tm, 0, ne)
                        se = str(v)
                        ne = QTableWidgetItem(se)
                        self.textEteil1.setItem(tm, ti, ne)
                        tm += 1

                        type_name = session.query('{0} where name is {1}'.format(v,k))
                        type_par = type_name[0]['parent']
                        name = type_par['name']
                        self.textEteil.setPlaceholderText(str(name))
            else:
                #二次返回
                a = len([k for k, v in project_dict.items()])
                self.textEteil1.setRowCount(a)
                for k, v in project_dict.items():
                    print k, v
                    if v == 'Sequence' or v == 'Folder' or v == 'Asset Build':
                        ne = QTableWidgetItem(k)
                        self.textEteil1.setItem(tm, 0, ne)
                        se = str(v)
                        ne = QTableWidgetItem(se)
                        self.textEteil1.setItem(tm, ti, ne)
                        tm += 1

                        type_name = session.query('{0} where name is {1}'.format(v, k))
                        type_par = type_name[0]['parent']
                        name = type_par['name']
                        self.textEteil.setPlaceholderText(str(name))



        # seq_dict.clear()
        # project_dict.clear()
        # print seq_dict



    #确定按钮
    def fix(self):
        window.lineEdit.setPlaceholderText('123')
        self.close()

    #退出子窗口
    def out(self):
        window.lineEdit.clear()
        self.close()


if __name__=='__main__':

    app = QApplication(sys.argv)

    # my = MyClass()
    # my.resize(300, 200)
    # my.setWindowTitle('Connect')
    # my.setWindowIcon(QIcon('image/C.png'))

    window=MainWindow()
    child=ChildWindow()
    window.resize(1300, 800)
    window.setWindowTitle('Connect')
    window.setWindowIcon(QIcon('image/C.png'))

    # 显示
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    #my.show()
    window.show()
    sys.exit(app.exec_())

