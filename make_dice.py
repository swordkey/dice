import random
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *





class Dice(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.LockButton = QPushButton("Shuffle")
        self.RollButton = QPushButton("Roll")
        img = QPixmap('dice1.png')
        self.lbl_img = QLabel()
        self.lbl_img.setPixmap(img)
        self.ran=0
        '''
        1.Lock버튼을 toggle로만들기
        2.Lock버튼의 초기값 True로
        3.Lock버튼의 초기스타일 지정
        4.Lock버튼과 토글 세부사항의 slot연결
        '''

        self.LockButton.setCheckable(True)
        self.LockButton.setChecked(True)
        self.LockButton.setStyleSheet("background-color: green")
        self.LockButton.toggled.connect(self.slot_toggle)
        
        '''
        주사위와 Lock버튼이 위아래로 정렬되도록 QVBOX생성후 그안에 넣음
        '''
        form_lbx = QBoxLayout(QVBoxLayout.TopToBottom, parent = self)
        self.setLayout(form_lbx)
        form_lbx.addWidget(self.LockButton)
        form_lbx.addWidget(self.lbl_img)

        '''주사위던지기 시그널을 clicked_method메소드와 연결'''
        Roll.rolldice.connect(self.clicked_method)

    @pyqtSlot(bool)
    def slot_toggle(self,state):

        self.LockButton.setStyleSheet("background-color: %s" % ({True: "green", False: "red"}[state]))
        self.LockButton.setText({True: "Shuffle", False: "Locked"}[state])

    def clicked_method(self):

        if self.LockButton.isChecked():
            self.ran = random.randint(1, 6)
            if self.ran == 1:
                img = QPixmap('dice1.png')
                self.lbl_img.setPixmap(img)
            elif self.ran == 2:
                img = QPixmap('dice2.png')
                self.lbl_img.setPixmap(img)
            elif self.ran == 3:
                img = QPixmap('dice3.png')
                self.lbl_img.setPixmap(img)
            elif self.ran == 4:
                img = QPixmap('dice4.png')
                self.lbl_img.setPixmap(img)
            elif self.ran == 5:
                img = QPixmap('dice5.png')
                self.lbl_img.setPixmap(img)
            elif self.ran == 6:
                img = QPixmap('dice6.png')
                self.lbl_img.setPixmap(img)

'''스코어'''
class dice_score(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        img = QPixmap('null.png')
        self.lbl_img1 = QLabel()
        self.lbl_img1.setPixmap(img)
        self.lbl_img2 = QLabel()
        self.lbl_img2.setPixmap(img)
        self.lbl_img3 = QLabel()
        self.lbl_img3.setPixmap(img)
        self.lbl_img4 = QLabel()
        self.lbl_img4.setPixmap(img)
        self.lbl_img5 = QLabel()
        self.lbl_img5.setPixmap(img)


        record = QBoxLayout(QBoxLayout.LeftToRight,parent=self)
        record.addWidget(self.lbl_img1)
        record.addWidget(self.lbl_img2)
        record.addWidget(self.lbl_img3)
        record.addWidget(self.lbl_img4)
        record.addWidget(self.lbl_img5)

class dice_score_form(QHBoxLayout):
    def __init__(self,upperform,rule_name):
        QWidget.__init__(self)

        self.score1 = dice_score()
        self.selected_rule1 = QRadioButton(upperform)
        self.rulename = QLabel(rule_name)


        self.addWidget(self.selected_rule1)
        self.addWidget(self.rulename)
        self.addWidget(self.score1)




'''메인 폼'''
class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.init_widget()



    def init_widget(self):

        self.chance = 3
        self.Total = 0

        ''' 주사위 5개 lbx에 추가'''
        form_lbx = QHBoxLayout()

        self.Dice1 = Dice()
        self.Dice2 = Dice()
        self.Dice3 = Dice()
        self.Dice4 = Dice()
        self.Dice5 = Dice()
        self.scoreform1 = dice_score_form(self,'Ones')
        self.scoreform2 = dice_score_form(self,'Twos')
        self.scoreform3 = dice_score_form(self,'Threes')
        self.scoreform4 = dice_score_form(self,'Fours')
        self.scoreform5 = dice_score_form(self,'Fives')
        self.scoreform6 = dice_score_form(self,'Sixes')
        self.scoreform7 = dice_score_form(self,'Choice')
        self.scoreform8 = dice_score_form(self,'4 of a Kind')
        self.scoreform9 = dice_score_form(self,'Full House')
        self.scoreform10 = dice_score_form(self, 'Little Straight')
        self.scoreform11 = dice_score_form(self, 'Big Straight')
        self.scoreform12 = dice_score_form(self, 'Yacht')
        self.curScore = QLabel('Current Selection:')
        self.TOTAL = QLabel('TOTAL:')



        scoreGroupH1 = QVBoxLayout()
        scoreGroupH2 = QVBoxLayout()
        scoreGroupH = QHBoxLayout()
        scoreGroup = QGroupBox()
        scoreGroupH1.addLayout(self.scoreform1)
        scoreGroupH1.addLayout(self.scoreform2)
        scoreGroupH1.addLayout(self.scoreform3)
        scoreGroupH1.addLayout(self.scoreform4)
        scoreGroupH1.addLayout(self.scoreform5)
        scoreGroupH1.addLayout(self.scoreform6)
        scoreGroupH1.addWidget(self.TOTAL)
        scoreGroupH2.addLayout(self.scoreform7)
        scoreGroupH2.addLayout(self.scoreform8)
        scoreGroupH2.addLayout(self.scoreform9)
        scoreGroupH2.addLayout(self.scoreform10)
        scoreGroupH2.addLayout(self.scoreform11)
        scoreGroupH2.addLayout(self.scoreform12)
        scoreGroupH2.addWidget(self.curScore)
        scoreGroupH.addLayout(scoreGroupH1)
        scoreGroupH.addLayout(scoreGroupH2)
        scoreGroup.setLayout(scoreGroupH)

        form_lbx.addWidget(scoreGroup)
        form_lbx.addWidget(self.Dice1)
        form_lbx.addWidget(self.Dice2)
        form_lbx.addWidget(self.Dice3)
        form_lbx.addWidget(self.Dice4)
        form_lbx.addWidget(self.Dice5)
        self.setLayout(form_lbx)

        self.RollButton = QPushButton('Roll 3/3')
        self.RecordButton = QPushButton('Record')


        form_lbx.addWidget(self.RollButton)
        form_lbx.addWidget(self.RecordButton)
        '''RollButton에 외부 시그널 연결
        시그널을 외부에 둔 이유는 Dice개체 5개를 한번에 컨트롤 하기위해서'''
        self.RollButton.clicked.connect(Roll.rolldice.emit)
        self.RecordButton.clicked.connect(self.keep_score)
        Roll.rolldice.connect(self.Chances)

    def Chances(self):

        self.chance = self.chance -1
        self.RollButton.setText('Roll ' + str(self.chance) + '/3')
        if self.chance == 0:
            self.RollButton.setDisabled(True)

    def keep_score(self):

        ran1 = self.Dice1.ran
        ran2 = self.Dice2.ran
        ran3 = self.Dice3.ran
        ran4 = self.Dice4.ran
        ran5 = self.Dice5.ran
        rank = [ran1,ran2,ran3,ran4,ran5]
        arr = [1,2,3,4,5,6]
        tmpscore = 0

        if self.scoreform1.selected_rule1.isChecked():
            self.scoreform1.score1.lbl_img1.setPixmap(QPixmap('dice' + str(ran1) + '.png'))
            self.scoreform1.score1.lbl_img2.setPixmap(QPixmap('dice' + str(ran2) + '.png'))
            self.scoreform1.score1.lbl_img3.setPixmap(QPixmap('dice' + str(ran3) + '.png'))
            self.scoreform1.score1.lbl_img4.setPixmap(QPixmap('dice' + str(ran4) + '.png'))
            self.scoreform1.score1.lbl_img5.setPixmap(QPixmap('dice' + str(ran5) + '.png'))
            self.curScore.setText('Current Selection : + ' + str(rank.count(1) * 1) + ' score')
            self.scoreform1.selected_rule1.setDisabled(True)
            tmpscore = rank.count(1) * 1


        elif self.scoreform2.selected_rule1.isChecked():
            self.scoreform2.score1.lbl_img1.setPixmap(QPixmap('dice' + str(ran1) + '.png'))
            self.scoreform2.score1.lbl_img2.setPixmap(QPixmap('dice' + str(ran2) + '.png'))
            self.scoreform2.score1.lbl_img3.setPixmap(QPixmap('dice' + str(ran3) + '.png'))
            self.scoreform2.score1.lbl_img4.setPixmap(QPixmap('dice' + str(ran4) + '.png'))
            self.scoreform2.score1.lbl_img5.setPixmap(QPixmap('dice' + str(ran5) + '.png'))
            self.curScore.setText('Current Selection : + ' + str(rank.count(2) * 2) + ' score')
            self.scoreform2.selected_rule1.setDisabled(True)
            tmpscore = rank.count(2) * 2
        elif self.scoreform3.selected_rule1.isChecked():
            self.scoreform3.score1.lbl_img1.setPixmap(QPixmap('dice' + str(ran1) + '.png'))
            self.scoreform3.score1.lbl_img2.setPixmap(QPixmap('dice' + str(ran2) + '.png'))
            self.scoreform3.score1.lbl_img3.setPixmap(QPixmap('dice' + str(ran3) + '.png'))
            self.scoreform3.score1.lbl_img4.setPixmap(QPixmap('dice' + str(ran4) + '.png'))
            self.scoreform3.score1.lbl_img5.setPixmap(QPixmap('dice' + str(ran5) + '.png'))
            self.curScore.setText('Current Selection : + ' + str(rank.count(3) * 3) + ' score')
            self.scoreform3.selected_rule1.setDisabled(True)
            tmpscore = rank.count(3) * 3
        elif self.scoreform4.selected_rule1.isChecked():
            self.scoreform4.score1.lbl_img1.setPixmap(QPixmap('dice' + str(ran1) + '.png'))
            self.scoreform4.score1.lbl_img2.setPixmap(QPixmap('dice' + str(ran2) + '.png'))
            self.scoreform4.score1.lbl_img3.setPixmap(QPixmap('dice' + str(ran3) + '.png'))
            self.scoreform4.score1.lbl_img4.setPixmap(QPixmap('dice' + str(ran4) + '.png'))
            self.scoreform4.score1.lbl_img5.setPixmap(QPixmap('dice' + str(ran5) + '.png'))
            self.curScore.setText('Current Selection : + ' + str(rank.count(4) * 4) + ' score')
            self.scoreform4.selected_rule1.setDisabled(True)
            tmpscore = rank.count(4) * 4
        elif self.scoreform5.selected_rule1.isChecked():
            self.scoreform5.score1.lbl_img1.setPixmap(QPixmap('dice' + str(ran1) + '.png'))
            self.scoreform5.score1.lbl_img2.setPixmap(QPixmap('dice' + str(ran2) + '.png'))
            self.scoreform5.score1.lbl_img3.setPixmap(QPixmap('dice' + str(ran3) + '.png'))
            self.scoreform5.score1.lbl_img4.setPixmap(QPixmap('dice' + str(ran4) + '.png'))
            self.scoreform5.score1.lbl_img5.setPixmap(QPixmap('dice' + str(ran5) + '.png'))
            self.curScore.setText('Current Selection : + ' + str(rank.count(5) * 5) + ' score')
            tmpscore =rank.count(5) * 5
            self.scoreform5.selected_rule1.setDisabled(True)
        elif self.scoreform6.selected_rule1.isChecked():
            self.scoreform6.score1.lbl_img1.setPixmap(QPixmap('dice' + str(ran1) + '.png'))
            self.scoreform6.score1.lbl_img2.setPixmap(QPixmap('dice' + str(ran2) + '.png'))
            self.scoreform6.score1.lbl_img3.setPixmap(QPixmap('dice' + str(ran3) + '.png'))
            self.scoreform6.score1.lbl_img4.setPixmap(QPixmap('dice' + str(ran4) + '.png'))
            self.scoreform6.score1.lbl_img5.setPixmap(QPixmap('dice' + str(ran5) + '.png'))
            self.curScore.setText('Current Selection : + ' + str(rank.count(6) * 6) + ' score')
            tmpscore = rank.count(6) * 6
            self.scoreform6.selected_rule1.setDisabled(True)
        elif self.scoreform7.selected_rule1.isChecked():
            self.scoreform7.score1.lbl_img1.setPixmap(QPixmap('dice' + str(ran1) + '.png'))
            self.scoreform7.score1.lbl_img2.setPixmap(QPixmap('dice' + str(ran2) + '.png'))
            self.scoreform7.score1.lbl_img3.setPixmap(QPixmap('dice' + str(ran3) + '.png'))
            self.scoreform7.score1.lbl_img4.setPixmap(QPixmap('dice' + str(ran4) + '.png'))
            self.scoreform7.score1.lbl_img5.setPixmap(QPixmap('dice' + str(ran5) + '.png'))
            self.curScore.setText('Current Selection : + ' + str(ran1+ran2+ran3+ran4+ran5) + ' score')
            tmpscore =ran1+ran2+ran3+ran4+ran5
            self.scoreform7.selected_rule1.setDisabled(True)
        elif self.scoreform8.selected_rule1.isChecked():
            self.scoreform8.score1.lbl_img1.setPixmap(QPixmap('dice' + str(ran1) + '.png'))
            self.scoreform8.score1.lbl_img2.setPixmap(QPixmap('dice' + str(ran2) + '.png'))
            self.scoreform8.score1.lbl_img3.setPixmap(QPixmap('dice' + str(ran3) + '.png'))
            self.scoreform8.score1.lbl_img4.setPixmap(QPixmap('dice' + str(ran4) + '.png'))
            self.scoreform8.score1.lbl_img5.setPixmap(QPixmap('dice' + str(ran5) + '.png'))
            self.curScore.setText('Current Selection : + ' + '0' + ' score')
            for a in arr:
                if rank.count(a) > 3:
                    self.curScore.setText('Current Selection : + ' + str(rank.count(a) * a) + ' score')
                    tmpscore =rank.count(a) * a
            self.scoreform8.selected_rule1.setDisabled(True)

        elif self.scoreform9.selected_rule1.isChecked():
            self.scoreform9.score1.lbl_img1.setPixmap(QPixmap('dice' + str(ran1) + '.png'))
            self.scoreform9.score1.lbl_img2.setPixmap(QPixmap('dice' + str(ran2) + '.png'))
            self.scoreform9.score1.lbl_img3.setPixmap(QPixmap('dice' + str(ran3) + '.png'))
            self.scoreform9.score1.lbl_img4.setPixmap(QPixmap('dice' + str(ran4) + '.png'))
            self.scoreform9.score1.lbl_img5.setPixmap(QPixmap('dice' + str(ran5) + '.png'))
            self.curScore.setText('Current Selection : + ' + '0' + ' score')
            for a in arr:
                if rank.count(a) > 2:
                    arr.remove(a)
                    for b in arr:
                        if rank.count(b) > 1:
                            self.curScore.setText('Current Selection : + ' + str(rank.count(a) * a + rank.count(b) * b) + ' score')
                            tmpscore = rank.count(a) * a + rank.count(b) * b
            self.scoreform9.selected_rule1.setDisabled(True)

        elif self.scoreform10.selected_rule1.isChecked():
            self.scoreform10.score1.lbl_img1.setPixmap(QPixmap('dice' + str(ran1) + '.png'))
            self.scoreform10.score1.lbl_img2.setPixmap(QPixmap('dice' + str(ran2) + '.png'))
            self.scoreform10.score1.lbl_img3.setPixmap(QPixmap('dice' + str(ran3) + '.png'))
            self.scoreform10.score1.lbl_img4.setPixmap(QPixmap('dice' + str(ran4) + '.png'))
            self.scoreform10.score1.lbl_img5.setPixmap(QPixmap('dice' + str(ran5) + '.png'))
            self.curScore.setText('Current Selection : + ' + '0' + ' score')
            self.scoreform10.selected_rule1.setDisabled(True)
            rank.sort()
            if rank == [1,2,3,4,5]:
                self.curScore.setText('Current Selection : + ' + '30' + ' score')
                tmpscore =30
        elif self.scoreform11.selected_rule1.isChecked():
            self.scoreform11.score1.lbl_img1.setPixmap(QPixmap('dice' + str(ran1) + '.png'))
            self.scoreform11.score1.lbl_img2.setPixmap(QPixmap('dice' + str(ran2) + '.png'))
            self.scoreform11.score1.lbl_img3.setPixmap(QPixmap('dice' + str(ran3) + '.png'))
            self.scoreform11.score1.lbl_img4.setPixmap(QPixmap('dice' + str(ran4) + '.png'))
            self.scoreform11.score1.lbl_img5.setPixmap(QPixmap('dice' + str(ran5) + '.png'))
            self.curScore.setText('Current Selection : + ' + '0' + ' score')
            rank.sort()
            if rank == [2,3,4,5,6]:
                self.curScore.setText('Current Selection : + ' + '30' + ' score')
                tmpscore =30
            self.scoreform11.selected_rule1.setDisabled(True)
        elif self.scoreform12.selected_rule1.isChecked():
            self.scoreform12.score1.lbl_img1.setPixmap(QPixmap('dice' + str(ran1) + '.png'))
            self.scoreform12.score1.lbl_img2.setPixmap(QPixmap('dice' + str(ran2) + '.png'))
            self.scoreform12.score1.lbl_img3.setPixmap(QPixmap('dice' + str(ran3) + '.png'))
            self.scoreform12.score1.lbl_img4.setPixmap(QPixmap('dice' + str(ran4) + '.png'))
            self.scoreform12.score1.lbl_img5.setPixmap(QPixmap('dice' + str(ran5) + '.png'))
            for a in arr:
                if rank.count(a) > 4:
                    self.curScore.setText('Current Selection : + ' + str(rank.count(a) * a) + ' score')
                    tmpscore=30
            self.scoreform12.selected_rule1.setDisabled(True)
        self.Total = self.Total + tmpscore
        self.TOTAL.setText('ToTal : ' + str(self.Total))
        self.RollButton.setEnabled(True)
        self.chance = 3
        self.RollButton.setText('Roll 3/3')

class RollDice(QObject):
    '''주사위 던지기 시그널 생성을 위한 객체'''
    rolldice = pyqtSignal()
'''주사위 던지기 시그널 외부 생성'''
Roll = RollDice()




'''수행문'''
if __name__ == "__main__":
    app = QApplication(sys.argv)
    yacht_dice = Form()
    yacht_dice.show()
    sys.exit(app.exec_())