import sys
from pathlib import Path
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

# ==============================================================================
# [과제 1 자기 설명 및 AI 사용 명시]
# 학번: 20230176
# 이름: 김민중
# Q1. State -> Event -> Action -> Update -> Feedback 설명:
# - State (상태): GUI 애플리케이션이 유지하고 있는 현재 데이터와 화면 구성 요소들의 상태입니다. 초기 상태에서는 프로필 사진(lbl_photo)이 숨겨져 있고(hide), 입력 필드와 세부 정보 라벨은 비어 있으며, 상태 라벨에는 초기 안내 문구가 설정되어 있습니다.
# - Event (이벤트): 사용자의 상호작용으로 발생하는 사건입니다. 본 프로그램에서는 사용자가 '학생증 발급' 버튼이나 '초기화' 버튼을 마우스로 클릭하는 클릭 이벤트(clicked)가 해당합니다.
# - Action (동작): 이벤트가 감지되었을 때 이를 처리하기 위해 호출되는 슬롯 메서드입니다. '학생증 발급' 클릭 시 on_click_issue()가 실행되고, '초기화' 클릭 시 on_click_clear()가 실행됩니다.
# - Update (갱신): Action 메서드 내에서 입력값을 검증하고, 학번에서 입학년도 추출, 자릿수 합(체크섬) 계산, 홀/짝수 구분에 따른 회원 등급 판정 등 내부 데이터와 위젯의 상태를 갱신합니다.
# - Feedback (피드백): 갱신된 결과를 사용자에게 시각적으로 보여주는 단계입니다. 상태 라벨에 발급 완료 문구를 띄우고, 프로필 사진을 화면에 표시(show)하며, 세부 정보 라벨에 입학년도, 인증코드, 등급을 출력하여 사용자에게 처리 결과를 즉각 전달합니다.
#
# Q2. 학번 인증코드 계산 로직 설명:
# - 사용자가 입력한 8자리 학번 문자열의 각 자릿수를 하나씩 숫자로 변환한 뒤 모두 더하여 합계(체크섬)를 구합니다.
# - 제 학번인 '20230176'의 경우: 2 + 0 + 2 + 3 + 0 + 1 + 7 + 6 = 21이 인증 코드가 됩니다.
# - 코드에서는 제너레이터 표현식을 활용해 sum(int(digit) for digit in student_id) 형태로 안전하고 간결하게 계산했습니다.
#
# Q3. AI 도구 사용 여부 및 수정 내용:
# - 사용 여부: Gemini 활용
# - 수정 내용: 학번 각 자릿수 합(체크섬) 계산 시 파이썬 내장 sum() 함수 문법 확인 및 입력값 유효성 검사 조건문 작성에 참고함.
# ==============================================================================

class StudentCardApp(QWidget):
    def __init__(self):
        super().__init__()
        # 이미지 경로 설정 (증명사진 파일 또는 profile.png 탐색)
        base_dir = Path(__file__).parent
        for candidate in ["증명사진.JPG", "증명사진.jpg", "증명사진.png", "profile.png"]:
            if (base_dir / candidate).exists():
                self.img_path = base_dir / candidate
                break
        else:
            self.img_path = base_dir / "profile.png"
        self.init_ui()

    def init_ui(self):
        # TODO 1: 윈도우 제목 설정 ("[학번] [이름] - 스마트 학생증 발급기") 및 창 크기 고정 (450 x 420)
        self.setWindowTitle("20230176 김민중 - 스마트 학생증 발급기")
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
        self.btn_issue.clicked.connect(self.on_click_issue)

        # 초기화 버튼
        self.btn_clear = QPushButton("초기화", self)
        self.btn_clear.resize(120, 35)
        self.btn_clear.move(235, 150)
        # TODO 3: btn_clear 클릭 시 on_click_clear 메서드 연결
        self.btn_clear.clicked.connect(self.on_click_clear)

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
        if not name:
            self.lbl_status.setText("이름을 입력해주세요.")
            self.lbl_info.setText("")
            self.lbl_photo.hide()
            return

        if len(student_id) != 8 or not student_id.isdigit():
            self.lbl_status.setText("학번 8자리 숫자를 올바르게 입력하세요.")
            self.lbl_info.setText("")
            self.lbl_photo.hide()
            return

        # TODO 5: 학번 앞 4자리로 입학년도 추출
        admission_year = student_id[:4]

        # TODO 6: 학번 8자리 숫자의 각 자릿수 합(체크섬) 계산
        checksum = sum(int(digit) for digit in student_id)

        # TODO 7: 학번 끝자리의 홀수/짝수 여부에 따라 등급 구분 ('BLUE 등급' 또는 'GOLD 등급')
        last_digit = int(student_id[-1])
        if last_digit % 2 != 0:
            grade = "BLUE 등급 (일반)"
        else:
            grade = "GOLD 등급 (우수)"

        # TODO 8: 결과 안내 문구 표시 및 profile.png 이미지를 QPixmap으로 로드하여 lbl_photo.show()
        self.lbl_status.setText(f"{name} 학생 ({admission_year}학번) 발급 완료! [인증코드: {checksum}]")
        self.lbl_info.setText(
            f"입학년도: {admission_year}학번\n"
            f"인증코드 (체크섬): {checksum}\n"
            f"회원 등급: {grade}"
        )

        if self.img_path.exists():
            pixmap = QPixmap(str(self.img_path))
            self.lbl_photo.setPixmap(pixmap)
            self.lbl_photo.setScaledContents(True)
            self.lbl_photo.show()

    def on_click_clear(self):
        # TODO 9: 입력창 지우기, 라벨 초기화, 사진 hide()
        self.le_name.clear()
        self.le_id.clear()
        self.lbl_status.setText("이름과 학번을 입력한 후 발급 버튼을 누르세요.")
        self.lbl_info.setText("")
        self.lbl_photo.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StudentCardApp()
    window.show()
    sys.exit(app.exec_())
