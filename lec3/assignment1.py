import sys
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

# ==============================================================================
# [과제 1 자기 설명 및 AI 사용 명시]
# 학번:
# 이름:
# Q1. State -> Event -> Action -> Update -> Feedback 설명:
#
# Q2. 학번 인증코드 계산 로직 설명:
#
# Q3. AI 도구 사용 여부 및 수정 내용:
#
# ==============================================================================

class StudentCardApp(QWidget):
    def __init__(self):
        super().__init__()
        # 이미지 경로 설정 (현재 파일과 같은 폴더의 profile.png)
        self.img_path = Path(__file__).parent / "profile.png"
        self.init_ui()

    def init_ui(self):
        # TODO 1: 윈도우 제목 설정 ("[학번] [이름] - 스마트 학생증 발급기") 및 창 크기 고정 (450 x 420)
        self.setWindowTitle("스마트 학생증 발급기")
        self.setFixedSize(450, 420)

        # 상태 안내 라벨
        self.lbl_status = QLabel("이름과 학번을 입력한 후 발급 버튼을 누르세요.", self)
        self.lbl_status.setAlignment(Qt.AlignCenter)
        self.lbl_status.resize(400, 30)
        self.lbl_status.move(25, 20)

        # 이름 입력 필드
        self.le_name = QLineEdit(self)
        self.le_name.setPlaceholderText("이름을 입력하세요")
        self.le_name.resize(250, 30)
        self.le_name.move(100, 60)

        # 학번 입력 필드
        self.le_id = QLineEdit(self)
        self.le_id.setPlaceholderText("학번 8자리를 입력하세요")
        self.le_id.resize(250, 30)
        self.le_id.move(100, 100)

        # 발급 버튼
        self.btn_issue = QPushButton("학생증 발급", self)
        self.btn_issue.resize(120, 35)
        self.btn_issue.move(95, 150)
        # TODO 2: btn_issue 클릭 시 on_click_issue 메서드 연결

        # 초기화 버튼
        self.btn_clear = QPushButton("초기화", self)
        self.btn_clear.resize(120, 35)
        self.btn_clear.move(235, 150)
        # TODO 3: btn_clear 클릭 시 on_click_clear 메서드 연결

        # 사진 표시 라벨
        self.lbl_photo = QLabel(self)
        self.lbl_photo.resize(120, 120)
        self.lbl_photo.move(165, 200)
        self.lbl_photo.hide()

        # 세부 정보 표시 라벨
        self.lbl_info = QLabel("", self)
        self.lbl_info.setAlignment(Qt.AlignCenter)
        self.lbl_info.resize(400, 60)
        self.lbl_info.move(25, 330)

    def on_click_issue(self):
        name = self.le_name.text().strip()
        student_id = self.le_id.text().strip()

        # TODO 4: 입력 검증 (이름이 비어있거나 학번이 8자리 숫자가 아닌 경우 오류 처리)

        # TODO 5: 학번 앞 4자리로 입학년도 추출

        # TODO 6: 학번 8자리 숫자의 각 자릿수 합(체크섬) 계산

        # TODO 7: 학번 끝자리의 홀수/짝수 여부에 따라 등급 구분 ('BLUE 등급' 또는 'GOLD 등급')

        # TODO 8: 결과 안내 문구 표시 및 profile.png 이미지를 QPixmap으로 로드하여 lbl_photo.show()

    def on_click_clear(self):
        # TODO 9: 입력창 지우기, 라벨 초기화, 사진 hide()
        pass

