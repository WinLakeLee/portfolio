PROJECTS = {
    "bros": {
        "id": "bros",
        "title": "BROS (Budget & Route Optimization System)",
        "subtitle": "종합 커뮤니티 & 경로 탐색 플랫폼",
        "category": "Team Project",
        "type": "Full Stack (React + Flask)",
        "summary": "커뮤니티 피드, 실시간 경로 탐색, 코스메틱 스토어를 결합한 소셜 플랫폼입니다. React(Vite) 프론트엔드와 Flask 백엔드로 구축되었습니다.",
        "github_links": [
            {"name": "Frontend GitHub", "url": "https://github.com/RCXD/Bros-front"},
            {"name": "Backend GitHub", "url": "https://github.com/RCXD/Bros-back"},
        ],
        "tech_stack": {
            "Frontend": [
                "React 19",
                "Vite",
                "Redux Toolkit",
                "React Query",
                "Leaflet",
                "Bootstrap",
            ],
            "Backend": [
                "Flask",
                "SQLAlchemy",
                "JWT",
                "OSRM (Navigation)",
                "GeoAlchemy2",
            ],
            "Infrastructure": ["Flask-Migrate", "Kakao/Google/Naver OAuth"],
            "Integrations": ["Kakao Pay", "Nominatim API", "Social Login"],
        },
        "features": [
            {
                "name": "커뮤니티 피드",
                "desc": "인스타그램 스타일의 소셜 피드로 무한 스크롤, 좋아요, 댓글, 상세 검색 기능을 지원합니다.",
            },
            {
                "name": "스마트 경로 탐색",
                "desc": "OSRM 기반 실시간 경로 계획, 위험 지역 알림, 다중 경유지 설정을 제공합니다.",
            },
            {
                "name": "코스메틱 스토어",
                "desc": "아이템 합성, 인벤토리 관리, 구매 절차를 포함한 가상 경제 시스템입니다.",
            },
            {
                "name": "고급 인증 시스템",
                "desc": "자동 토큰 갱신 기능이 있는 강력한 JWT 인증 및 다중 제공자(Google, Kakao, Naver) OAuth를 지원합니다.",
            },
            {
                "name": "관리자 콘솔",
                "desc": "사용자 관리, 콘텐츠 모니터링, 시스템 통계를 위한 종합 대시보드입니다.",
            },
        ],
        "role": "Core Developer (Map, Auth, Store)",
        "role_summary": "Leaflet 지도 UI를 독자적으로 구현하고, OSRM과 MySQL Geometry를 활용해 스마트 경로 탐색 로직을 완성했습니다. 또한, 인증 및 코스메틱 스토어의 핵심 기능을 주도했습니다.",
        "contribution_points": [
            {
                "title": "지도/경로 탐색 (기여도 100%)",
                "desc": "Leaflet 라이브러리를 사용해 지도 UI를 독자적으로 구현했습니다. 백엔드에서는 OSRM 엔진과 MySQL Geometry 함수를 활용하여 스마트 경로 탐색 로직을 완성했습니다.",
            },
            {
                "title": "코스메틱 스토어",
                "desc": '프로필 이미지 위에 아이템 이미지를 레이어링(Overlay)하는 방식으로 "꾸미기" 기능을 구현했습니다.',
            },
            {
                "title": "인증 시스템",
                "desc": "JWT 기반 로그인을 구현했으며, 로그인 응답 시 단순 토큰뿐만 아니라 포인트, 회원번호 등 초기 구동에 필요한 필수 데이터를 포함시켜 클라이언트의 추가 요청을 최소화했습니다.",
            },
        ],
        "lessons": "OSRM과 Leaflet을 연동하여 커스텀 경로 탐색 기능을 구현하며 GIS(지리 정보 시스템) 데이터 처리에 대한 깊은 이해를 얻었습니다. 또한 MySQL의 Geometry 함수를 활용하여 공간 데이터를 효율적으로 쿼리하는 방법을 익혔습니다.",
        "improvements": "현재 코스메틱 아이템 착용 시 클라이언트에서 이미지를 겹쳐서 표현하고 있는데, 추후 서버에서 합성된 이미지를 생성하여 전송하는 방식으로 변경하면 클라이언트 렌더링 부하를 줄일 수 있을 것으로 보입니다.",
        "details": """
            BROS는 소셜 경험과 유틸리티 기능을 통합한 대규모 풀스택 프로젝트입니다.
            **Frontend**는 사용자가 풍부한 지도 인터페이스를 탐색하고, 피드 시스템을 통해 타인과 소통하며, 코스메틱 아이템으로 경험을 사용자 정의할 수 있게 합니다.
            **Backend**는 Flask의 Blueprint 아키텍처를 기반으로 구축되어, 인증, 게시물, 장소, 결제 등 다양한 서비스 간의 모듈성을 보장합니다.
        """,
    },
    "404-ai": {
        "id": "404-ai",
        "title": "404-AI Operations",
        "subtitle": "자동화된 산업용 이상 탐지 시스템",
        "category": "Team Project",
        "type": "AI/ML Backend",
        "summary": "산업 품질 관리를 위한 고성능 이상 탐지 서버로, 객체 감지를 위한 YOLO/FastSAM과 결함 식별을 위한 PatchCore를 활용합니다.",
        "github_links": [
            {"name": "GitHub Repository", "url": "https://github.com/WinLakeLee/404-ai"}
        ],
        "tech_stack": {
            "Core": ["Flask", "Python 3.10+"],
            "AI/ML": ["YOLO", "FastSAM", "PatchCore", "EfficientAD"],
            "IoT/Messaging": ["MQTT", "REST API"],
            "Tools": ["PyTorch", "Numpy", "OpenCV", "Ultralytics"],
        },
        "features": [
            {
                "name": "듀얼 감지 엔진",
                "desc": "유연한 객체 감지 요구 사항을 위해 YOLO와 FastSAM을 모두 지원합니다.",
            },
            {
                "name": "PatchCore 이상 탐지",
                "desc": "미세한 결함을 식별할 수 있는 최첨단 비정형 결함 탐지 기술을 적용했습니다.",
            },
            {
                "name": "실시간 MQTT",
                "desc": "MQTT 프로토콜을 통해 검사 결과를 산업 제어 시스템(ICS)으로 즉시 전송합니다.",
            },
            {
                "name": "구성 가능한 파이프라인",
                "desc": "환경 변수를 통해 감지 임계값 및 모델 매개변수를 세밀하게 조정할 수 있습니다.",
            },
            {
                "name": "상태 모니터링",
                "desc": "운영 환경에서의 신뢰성을 보장하기 위한 내장 시스템 상태 확인 기능을 제공합니다.",
            },
        ],
        "role": "AI/ML Engineer",
        "role_summary": "YOLO/FastSAM과 PatchCore를 결합한 하이브리드 감지 엔진을 개발하고, 산업 현장 적용을 위한 MQTT 통신 파이프라인을 구축했습니다.",
        "contribution_points": [
            {
                "title": "듀얼 감지 엔진 개발",
                "desc": "객체 감지를 위한 YOLO/FastSAM과 이상 탐지를 위한 PatchCore 모델을 파이프라인으로 연결하여 정밀한 결함 검출 로직을 구현했습니다.",
            },
            {
                "title": "실시간 데이터 파이프라인",
                "desc": "MQTT 프로토콜을 활용하여 검사 결과를 지연 없이 공장 제어 시스템(PLC/PC)으로 전송하는 비동기 통신 구조를 설계했습니다.",
            },
            {
                "title": "유연한 설정 시스템",
                "desc": "현장 상황에 맞춰 감지 임계값(Threshold)과 모델 파라미터를 환경 변수로 실시간 조정할 수 있는 동적 설정 기능을 개발했습니다.",
            },
        ],
        "lessons": "서로 다른 딥러닝 모델(Detection + Anomaly)을 하나의 파이프라인으로 통합하며 메모리 관리와 추론 속도 최적화의 중요성을 배웠습니다. 또한 실제 산업용 프로토콜인 MQTT를 다루며 엣지 컴퓨팅 환경에 대한 이해를 넓혔습니다.",
        "improvements": "현재는 단일 이미지 처리에 집중되어 있으나, 향후 비디오 스트림을 실시간으로 처리할 수 있도록 배치 처리 또는 비동기 큐 시스템을 도입하여 처리량을 늘릴 계획입니다.",
        "details": """
            404-AI는 스마트 팩토리 환경을 위해 설계된 전문 엣지 서버 애플리케이션으로, 시각 검사 시스템의 두뇌 역할을 합니다.
        """,
    },
    "teamtest": {
        "id": "teamtest",
        "title": "Teamtest (Quiz & Market API)",
        "subtitle": "Spring Boot 기반 퀴즈 게임 및 마켓 백엔드",
        "category": "Team Project",
        "type": "Backend API",
        "summary": "퀴즈 게임 로직, 아이템 마켓, 랭킹 시스템을 제공하는 REST API 서버입니다. Spring Security와 JWT를 활용한 보안 및 소셜 로그인을 지원합니다.",
        "tech_stack": {
            "Framework": ["Java 21", "Spring Boot 3.5.5", "Spring Security"],
            "Database": ["MySQL", "Spring Data JPA"],
            "Auth": ["JWT", "OAuth2 (Kakao)", "Spring Security"],
            "Tools": ["Gradle", "Lombok"],
        },
        "features": [
            {
                "name": "퀴즈 시스템",
                "desc": "다양한 유형의 퀴즈 문제 출제 및 정답 채점 로직 (QuizController, Service).",
            },
            {
                "name": "아이템 마켓",
                "desc": "게임 내 재화를 이용한 아이템 구매 및 거래 시스템 (MarketService).",
            },
            {"name": "랭킹 시스템", "desc": "유저 점수 기반 실시간 순위 산정."},
            {
                "name": "소셜 로그인",
                "desc": "Kakao OAuth2 연동 및 JWT 토큰 기반 인증 처리.",
            },
        ],
        "role": "Backend Lead",
        "role_summary": "팀의 백엔드 리드로서 데이터베이스 스키마 설계(User, Quiz, Market, Item 등)부터 API 구현, 배포까지 전 과정을 주도했습니다.",
        "contribution_points": [
            {
                "title": "인증(Authentication)",
                "desc": "Spring Security Filter Chain을 커스터마이징하여 OAuth2 로그인 후 JWT를 발급하는 로직을 구현했습니다.",
            },
            {
                "title": "비즈니스 로직",
                "desc": "퀴즈 정답 확인, 점수 부여, 아이템 구매 트랜잭션 등 핵심 게임 로직을 서비스 레이어에 캡슐화했습니다.",
            },
            {
                "title": "예외 처리",
                "desc": "GlobalExceptionHandler를 통해 통일된 에러 응답 포맷을 정의하여 프론트엔드와의 협업 효율을 높였습니다.",
            },
        ],
        "lessons": "Spring Boot 3버전과 Java 21의 새로운 기능을 도입하며 최신 백엔드 트렌드를 학습했습니다. 특히 OAuth2와 JWT를 결합한 무상태(Stateless) 인증 아키텍처를 설계하며 보안에 대한 이해를 높였습니다.",
        "improvements": "초기 설계 시 트래픽 부하를 고려한 캐싱 전략(Redis 등)이 부재하여 랭킹 조회 시 DB 부하가 발생할 수 있음이 확인되었습니다. 추후 Redis 도입을 통해 성능 개선을 계획하고 있습니다.",
        "details": """
            이 프로젝트는 퀴즈 풀이와 마켓 경제가 결합된 게이미피케이션 플랫폼의 백엔드 서버입니다.
        """,
    },
    "obj-dct-seg": {
        "id": "obj-dct-seg",
        "title": "AI Defect Detection System",
        "subtitle": "딥러닝 기반 산업용 불량 검출 시스템",
        "category": "Personal Work",
        "type": "AI/ML Computer Vision",
        "summary": "YOLO와 Anomalib(PatchCore)을 활용하여 제조 공정의 불량을 실시간으로 감지하는 프로젝트입니다.",
        "github_links": [
            {
                "name": "GitHub Repository",
                "url": "https://github.com/WinLakeLee/obj-dct-seg",
            }
        ],
        "tech_stack": {
            "Core": ["Python 3.10", "Flask"],
            "AI/ML": [
                "Torch & Torchvision",
                "Ultralytics (YOLO)",
                "Anomalib (PatchCore)",
            ],
            "Vision": ["OpenCV"],
        },
        "features": [
            {
                "name": "AI 기반 불량 검출",
                "desc": "YOLO로 부품 위치를 찾고, Anomalib으로 정밀하게 불량 여부를 판단하는 통합 파이프라인 제공.",
            },
            {
                "name": "실시간 영상 처리",
                "desc": "카메라 스트림을 실시간으로 분석하여 즉각적인 불량 식별 가능.",
            },
            {
                "name": "웹 API 통합",
                "desc": "Flask 기반의 REST API 구조를 통해 외부 시스템과 연동 용이.",
            },
            {
                "name": "간편한 학습",
                "desc": "사용자 데이터셋을 이용해 YOLO 및 이상 탐지 모델을 쉽게 재학습할 수 있는 스크립트 포함.",
            },
        ],
        "role": "Solo Researcher & Developer",
        "role_summary": "산업용 데이터셋(MVTec 등)을 활용하여 다양한 이상 탐지 모델을 실험하고, 이를 실제 애플리케이션으로 서빙할 수 있는 전체 파이프라인을 구축했습니다.",
        "contribution_points": [
            {
                "title": "모델 실험 및 최적화",
                "desc": "EfficientAD, PatchCore 등 최신 SOTA 모델들을 비교 분석하고, Docker 컨테이너 환경에서 안정적으로 동작하도록 최적화했습니다.",
            },
            {
                "title": "아키텍처 설계",
                "desc": "Flask 기반의 Orchestrator와 개별 AI 서비스를 마이크로서비스 형태로 설계하여 유지보수성을 높였습니다.",
            },
        ],
        "lessons": "다양한 비전 모델의 특성과 장단점을 깊이 이해하게 되었으며, 연구 단계의 코드를 실제 서비스 가능한 형태(Docker API)로 패키징하는 MLOps 역량을 길렀습니다.",
        "improvements": "현재는 로컬 환경에서의 추론에 최적화되어 있으나, 향후 클라우드 환경(AWS, GCP)에서의 배포 및 오토스케일링을 고려한 설계를 추가하고 싶습니다.",
        "details": """
            이 프로젝트는 딥러닝과 컴퓨터 비전 기술을 활용하여 제조 공정 중 발생하는 불량을 실시간으로 감지하는 시스템입니다.
            
            **YOLO (Ultralytics)** 를 사용하여 불량 검사 대상 영역(ROI)을 탐지하고, **Anomalib (PatchCore)** 알고리즘을 통해 미세한 스크래치나 파손 같은 이상 징후를 판별합니다.
            
            단순한 모델 학습을 넘어, 실제 현장에 배포 가능한 형태의 소프트웨어 구조를 고민하며 설계했습니다.
            Detector, Inference, Orchestrator로 서비스를 분하여 각 기능의 독립성을 보장하고, Docker Compose를 통해 손쉽게 배포할 수 있는 환경을 구성했습니다.
        """,
    },
}


USER_PROFILE = {
    "name": "WinLakeLee",
    "email": "lst2413@gmail.com",
    "phone": "010-5503-5413",
    "address": "chuncheon, South Korea",
    "education": {
        "institution": "한림대학교",
        "majors": [
            {"label": "경제학", "url": "https://econo.hallym.ac.kr/econo/index.do"},
            {"label": "일본학", "url": "https://japanese.hallym.ac.kr/"},
        ],
    },
    "github_url": "https://github.com/WinLakeLee",
    "training_groups": [
        {
            "organization": "MBC 컴퓨터아카데미 천호",
            "details": ["AI를 활용한 웹 플랫폼 구축 과정 수료"],
        },
    ],
    "tech_stack_summary": {
        "Languages": [
            {"name": "Python", "icon": "fa-brands fa-python", "highlight": True},
            {"name": "Java", "icon": "fa-brands fa-java", "highlight": True},
            {"name": "JavaScript", "icon": "fa-brands fa-js", "highlight": True},
            {"name": "SQL", "icon": "fa-solid fa-database", "highlight": False},
            {"name": "HTML/CSS", "icon": "fa-brands fa-html5", "highlight": False},
        ],
        "Frontend & Mobile": [
            {"name": "React", "icon": "fa-brands fa-react", "highlight": True},
            {"name": "Vite", "icon": "fa-solid fa-bolt", "highlight": False},
            {"name": "Redux", "icon": "fa-solid fa-layer-group", "highlight": False},
            {"name": "Bootstrap", "icon": "fa-brands fa-bootstrap", "highlight": False},
            {
                "name": "Leaflet",
                "icon": "fa-solid fa-map-location-dot",
                "highlight": False,
            },
        ],
        "Backend & Database": [
            {"name": "Flask", "icon": "fa-solid fa-flask", "highlight": True},
            {"name": "Spring Boot", "icon": "fa-solid fa-leaf", "highlight": True},
            {"name": "SQLAlchemy", "icon": "fa-solid fa-link", "highlight": False},
            {"name": "JPA", "icon": "fa-solid fa-link", "highlight": False},
            {"name": "MySQL", "icon": "fa-solid fa-server", "highlight": False},
            {
                "name": "JWT / OAuth2",
                "icon": "fa-solid fa-shield-halved",
                "highlight": False,
            },
        ],
        "AI / ML & Vision": [
            {
                "name": "PyTorch",
                "icon": "fa-solid fa-fire-flame-curved",
                "highlight": True,
            },
            {"name": "YOLO", "icon": "fa-solid fa-eye", "highlight": False},
            {"name": "PatchCore", "icon": "fa-solid fa-microscope", "highlight": False},
            {"name": "Anomalib", "icon": "fa-solid fa-brain", "highlight": False},
            {"name": "OpenCV", "icon": "fa-solid fa-camera", "highlight": False},
        ],
        "Infrastructure & Tools": [
            {"name": "Docker", "icon": "fa-brands fa-docker", "highlight": True},
            {"name": "AWS", "icon": "fa-brands fa-aws", "highlight": False},
            {"name": "Git", "icon": "fa-brands fa-git-alt", "highlight": False},
            {"name": "MQTT", "icon": "fa-solid fa-tower-broadcast", "highlight": False},
            {"name": "Gradle", "icon": "fa-solid fa-hammer", "highlight": False},
            {"name": "OSRM", "icon": "fa-solid fa-route", "highlight": False},
        ],
    },
}


def get_all_projects_summary():
    """Returns a list of project summaries for list views."""
    return [
        {
            "id": p["id"],
            "title": p["title"],
            "subtitle": p["subtitle"],
            "category": p.get("category", "Other"),
            "type": p["type"],
            "summary": p["summary"],
            "tech_list": list(p["tech_stack"].keys()),
        }
        for p in PROJECTS.values()
    ]


def get_project_by_id(pid):
    """Returns full details for a specific project."""
    return PROJECTS.get(pid)


def get_profile_data():
    """Returns basic profile information."""
    return USER_PROFILE
