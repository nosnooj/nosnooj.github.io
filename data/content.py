# -*- coding: utf-8 -*-
"""
포트폴리오 콘텐츠 단일 소스 (Single Source of Truth).

모든 페이지(홈·케이스 스터디)는 이 모듈에서만 데이터를 읽는다.
원본: 손준혁_이력서.md. CS2~CS5 본문은 이력서 작성 진행에 맞춰 채운다.
"""

SITE = {
    "name": "손준혁",
    "role": "백엔드 개발자 · 데이터 흐름 설계",
    "kicker": "BACKEND ENGINEER · DATA FLOW DESIGN",
    "bio_line": "랩지노믹스 IT팀 선임 · 백엔드 개발 경력 7년+",
    "positioning": (
        "장비 연동, 주문·결제 트랜잭션, ERP, 인프라까지 — 도메인이 달라도 본질은 하나, "
        "데이터가 안정적으로 흐르는 구조를 설계합니다. 증상이 아니라 원인을 추적하는 방식으로 "
        "시스템을 만듭니다."
    ),
    "work_intro": (
        "장비 연동부터 B2B·B2C 서비스, 그 아래 인프라까지 5개 프로젝트입니다. "
        "도메인은 달라도 데이터 흐름과 상태를 안전하게 설계한다는 본질은 같습니다 — "
        "각 카드를 열면 케이스 스터디로 이어집니다."
    ),
    "contacts": {
        "email": "zlfm48@gmail.com",
        "github": "github.com/nosnooj",
        "github_url": "https://github.com/nosnooj",
        "site": "nosnooj.github.io",
        "site_url": "https://nosnooj.github.io",
        "resume_pdf": "",  # 최신 이력서 PDF 업로드 후 경로 지정 (예: assets/pdf/손준혁_이력서.pdf)
    },
    "metrics": [
        {"value": "0건", "label": "운영 이관 오류"},
        {"value": "95%", "label": "결과지 처리 단축"},
        {"value": "46%", "label": "인프라 비용 절감"},
        {"value": "99.9%", "label": "시스템 가용성"},
    ],
    "about": {
        "lede": (
            "통계학 석사 배경에서 데이터 분석으로 커리어를 시작해, 현재는 유전체·헬스케어 IT에서 "
            "장비 연동 LIMS 구축부터 AWS 아키텍처 전환까지 백엔드 전 구간을 맡고 있습니다. "
            "Java/Spring 기반의 장비 연동·결제·ERP 연동에서 데이터 정합성을 보장하고, "
            "State Machine·예외 계층화·AOP 설계로 근본 원인 중심의 장애 대응 구조를 만듭니다."
        ),
        "career": [
            {
                "period": "2023.12 ~ 재직 중",
                "company": "(주)랩지노믹스",
                "role": "선임 · IT팀 · 백엔드 개발",
                "points": [
                    "유전자 분석 장비(GeneTitan) 연동 Microarray LIMS 신규 구축 — MQTT 상태 수집·"
                    "WebSocket 결과 이관·비동기 병렬 처리, 동기화 오류 0건 달성",
                    "결과지 자동생성(GAIA) 처리시간 95% 단축, 주문·결제 백오피스(COS) 30% 단축, "
                    "ERP 연동(LESS) 반복업무 40% 절감",
                    "온프레미스 → AWS 아키텍처 전환 및 운영 이슈 100여 건 해결 — 인프라 비용 46% 절감, "
                    "가용성 99.9% 이상 확보",
                ],
            },
            {
                "period": "2022.02 ~ 2023.11",
                "company": "(주)제노코어비에스",
                "role": "주임 · AI분석개발팀 · 백엔드 개발",
                "points": [
                    "PHR·유전자 데이터 기반 B2C 영양제/보험 추천 플랫폼 신규 구축(PHP·MySQL), "
                    "개인화 추천 알고리즘 및 KCP 결제 연동",
                    "ClipSoft Report 도입 및 템플릿·데이터 매핑 계층 분리 설계 — 결과지 양식 변경을 "
                    "코드 배포 없이 처리 가능한 구조로 전환, 결과지 생성·수정·관리 자동화",
                ],
            },
            {
                "period": "2018.06 ~ 2022.04",
                "company": "Epsilon Data Management, LLC",
                "role": "Contractor · Technology Team",
                "points": [
                    "미국 SearchForce 인턴십 종료 후 Epsilon 합병에 따라 계약직으로 전환, 귀국 후 "
                    "한국에서 원격근무로 업무 지속",
                    "수백만 건 광고 데이터의 익월 예산 산정과 100여 개 계정 Invoice 문서 생성을 "
                    "Excel·VBA 매크로와 Python 크롤링·캡처 도구로 반자동화 — 반복 업무 시간 대폭 단축",
                    "광고 플랫폼 운영 이슈를 Oracle SQL 대용량 데이터 분석으로 원인 규명 및 해결",
                ],
            },
        ],
        "skills": [
            {"label": "Language", "items": ["Java", "Python", "PHP", "JavaScript", "SQL"]},
            {"label": "Backend", "items": ["Spring Boot", "Spring Security", "Spring AOP",
                                            "MyBatis", "JPA", "MQTT", "WebSocket",
                                            "CompletableFuture", "Thymeleaf", "FastAPI"]},
            {"label": "Database", "items": ["MS SQL Server", "MySQL", "Oracle"]},
            {"label": "Infra · DevOps", "items": ["AWS (EC2·S3·ELB)", "Linux", "Nginx",
                                                   "Redis", "Podman", "Docker",
                                                   "CI/CD (GitHub Actions·rsync)"]},
            {"label": "기타", "items": ["Azure OAuth2 SSO", "KCP 결제 연동", "ClipSoft", "Git/GitHub"]},
        ],
        "education": [
            {
                "period": "2019.03 ~ 2021.02",
                "title": "고려대학교 세종캠퍼스 · 응용통계학 석사",
                "detail": "학점 4.35 / 4.5 · 논문 «Bayesian inference for hidden stage "
                          "with distributed time delay»",
            },
            {
                "period": "2011.03 ~ 2017.02",
                "title": "대구대학교 · 전산통계학과 학사 (복수전공: 경영학과)",
                "detail": "학점 4.1 / 4.5",
            },
        ],
        "certs": [
            {"date": "2016.08", "title": "SAS Certified Predictive Modeler Using SAS Enterprise Miner 13",
             "meta": "SAS Institute · PMEM000721v13"},
            {"date": "2016.07", "title": "SAS Certified Advanced Programmer for SAS 9",
             "meta": "SAS Institute · AP017864v9"},
            {"date": "2015.07", "title": "SAS Certified Base Programmer for SAS 9",
             "meta": "SAS Institute · BP050880v9"},
            {"date": "2015.02", "title": "SAS Certified Statistical Business Analyst Using SAS 9",
             "meta": "SAS Institute · SBARM001510v9"},
            {"date": "2024.09", "title": "TOEIC 935", "meta": "LC 495 / RC 440"},
        ],
        "etc": [
            {"date": "2017.01 ~ 2018.06", "title": "한미 대학생 연수(WEST) 프로그램 · 국립국제교육원 선발",
             "detail": "POLY Languages Institute 어학 과정 수료 후 SearchForce, Inc.(San Mateo, CA) "
                       "기술서비스팀 인턴 → 정규 채용 제안 → Epsilon 원격 Contractor 근속"},
            {"date": "2014.11", "title": "2014학년도 제2학기 영어능력경시대회 10위",
             "detail": "대구대학교 외국어교육센터"},
            {"date": "2012.08", "title": "제6기 창의적 학습공동체 대상",
             "detail": "대구대학교 교무처 교육개발센터"},
            {"date": "2012.07 ~ 2014.04", "title": "병역 · 육군 병장 만기전역", "detail": ""},
        ],
    },
}


# ---------------------------------------------------------------------------
# 프로젝트 (케이스 스터디)
# ---------------------------------------------------------------------------
PROJECTS = [
    {
        "id": "cs1",
        "slug": "lims",
        "code": "CS1",
        "accent": "teal",
        "name": "Microarray LIMS · 결과지 자동화",
        "period": "2024.07 ~ 2025.09",
        "card_one_liner": "장비 연동부터 결과지 생성까지 단일 시스템화 — 이관 오류 0건",
        "card_stack": ["Java", "Spring", "MQTT", "WebSocket"],
        "status": "full",
        "hero": {
            "kicker": "CASE STUDY · CS1 · 2024.07–2025.09",
            "title": "장비에서 결과지까지, 손이 닿지 않는 흐름",
            "sub": "랩지노믹스 IT팀 · Microarray LIMS 신규 구축",
        },
        "figures": [
            {"cap": "FIG.A — 시스템 아키텍처 (내부망 분석 서버 / 외부 웹 호스팅 DMZ 분리)",
             "file": "cs1_arch.svg"},
        ],
        "glance": {
            "role": "팀장과 전체 설계 주도 · 수집·이관(A1)·판독·LIS 연동(A3)·결과지/모니터링 웹(B) 개발",
            "period": "2024.07 – 2025.09",
            "stack": ["Java", "Spring Boot", "Spring Security", "MQTT", "WebSocket",
                      "CompletableFuture", "AOP", "Thymeleaf", "MySQL", "MS SQL Server",
                      "Crownix Report (ClipSoft)"],
            "key_result": "수작업 파일 이관·점검 제거, 운영 이관 오류 0건",
        },
        "problem": (
            "유전자 분석 장비가 만들어 낸 대용량 결과 파일을 사람이 직접 분석 서버로 옮기고 "
            "이상 여부를 점검해야 했습니다. 분석은 단계별로 10분~3시간이 걸리는데 진행 상태가 "
            "여러 곳에 흩어져 있어 오류·지연 파악이 늦었고, 결과지는 수작업으로 생성해 처리 시간이 "
            "길고 누락·전달 오류 위험이 있었습니다. 검사 한 건이 결과지가 되기까지 사람의 손이 "
            "여러 번 개입하는 구조였습니다."
        ),
        "decisions": [
            {"head": "상태와 대용량 전송을 분리한다",
             "body": "실시간 진행률·오류 같은 가벼운 상태는 MQTT publish/subscribe로 구독·수집하고, "
                     "수백 MB~수 GB 결과 파일은 WebSocket으로 분석 서버에 전송합니다. "
                     "전송은 CompletableFuture로 병렬화해 다수 파일을 동시에 처리합니다."},
            {"head": "분석 진행을 명시적 State Machine으로 고정한다",
             "body": "Run 상태를 QUEUED → RUNNING → COMPLETED / FAILED / RETRY로 명시 정의하고 "
                     "비정상 전이를 차단합니다. 제한된 서버 자원 안에서 스레드 풀로 작업을 스케줄링합니다."},
            {"head": "내부망과 외부 공유 영역을 물리적으로 나눈다",
             "body": "분석 서버(LIMS 코어)는 내부망 전용, 결과지 생성·다운로드·검사 모니터링 웹은 "
                     "외부 공유 웹 호스팅 서버(DMZ)로 분리해 의뢰기관·외부 사용자 접근 경로를 격리합니다. "
                     "두 서버 모두 LIMS DB(MySQL)를 참조합니다."},
        ],
        "build": [
            {"module": "A1 — 장비 상태 실시간 수집 · 대용량 결과 이관",
             "points": [
                 "MQTT(Subscribe/Publish)로 장비 Run 상태(진행률·오류)를 실시간 구독·수집해 모니터링에 반영",
                 "Run 종료 시 대용량 결과 파일을 WebSocket으로 분석 서버에 전송, "
                 "CompletableFuture 병렬 전송으로 다수 파일 동시 처리 → 이관 시간 25~30분 → 약 5분",
                 "이관 과정의 중복·충돌·경로 오류를 유형별로 방어 → 운영 환경 이관 오류 0건",
             ]},
            {"module": "A2 — 분석 파이프라인 작업 오케스트레이션",
             "points": [
                 "이관된 샘플이 다단계 파이프라인(단계별 10분~3시간)을 자동 수행하도록 작업 관리·모니터링 체계 설계",
                 "제한된 서버 자원 내 스레드 풀 병렬 처리로 분석 작업 스케줄링",
                 "Run 상태를 명시적 State(QUEUED→RUNNING→COMPLETED/FAILED/RETRY)로 정의해 비정상 전이 차단",
             ]},
            {"module": "A3 — 결과 판독 웹 · 수진자 매핑 · LIS 양방향 연동",
             "points": [
                 "파이프라인 산출물을 DB 적재 후, 분석자가 수치형·이미지 데이터를 판독·입력·메모하는 "
                 "결과 판독 웹 구축(Audit·로그 포함)",
                 "수진자 매핑 데몬 개발 — 수진자 ID만 매핑하면 LIS에서 정보를 자동 조회·연계(LIMS/LIS DB 분리 운영)",
                 "판독 완료 결과를 LIS로 연동하는 데몬 구축 → 장비→판독→LIS 흐름을 양방향 자동 연계, "
                 "시스템 간 이중 입력·수작업 매핑 제거",
             ]},
            {"module": "B — 결과지 자동 생성 데몬 · 다운로드 · 검사 모니터링",
             "points": [
                 "ClipSoft Crownix Report로 최종 처리된 샘플 결과지를 매시간 자동 생성하는 스케줄 데몬 구축",
                 "수진자 정보 변경·결과 재입력 시 API 호출로 해당 결과지만 자동 재생성 → 처리시간 20분 → 1분 이내(95% 단축)",
                 "재채혈 요청·검사취소·고위험군·양성 판정 등 특이 소견을 한 화면에서 즉시 식별하는 모니터링 페이지 구축",
             ]},
            {"module": "공통 기반",
             "points": [
                 "Azure OAuth2 SSO · 메뉴 ACL로 접근 제어",
                 "AOP Audit 로깅으로 QA 감사 추적",
                 "GlobalExceptionHandler · BusinessException으로 예외 처리 일원화",
             ]},
        ],
        "result": {
            "metrics": [
                {"value": "0건", "label": "운영 이관 오류"},
                {"value": "25~30→5분", "label": "대용량 결과 이관"},
                {"value": "95%", "label": "결과지 20→1분"},
                {"value": "즉시 식별", "label": "특이 소견"},
            ],
            "retro": "상태·전송·예외를 계층으로 분리하니, 장애가 나도 '어느 단계에서 멈췄는가'가 "
                     "바로 드러나 원인 추적 시간이 짧아졌습니다.",
        },
    },
    {
        "id": "cs2", "slug": "less", "code": "CS2", "accent": "blue",
        "name": "LIS–ERP 연동 웹플랫폼 (LESS)",
        "period": "2024.04 ~ 2024.10",
        "card_one_liner": "검사–회계 데이터 흐름 연동 — 반복업무 절감",
        "card_stack": ["Java", "Spring", "ERP 연동"],
        "status": "skeleton",
        "hero": {"kicker": "CASE STUDY · CS2 · 2024.04–2024.10",
                 "title": "LIS–ERP 연동 웹플랫폼 (LESS)", "sub": "랩지노믹스 IT팀"},
        "figures": [{"cap": "FIG.A — LIS–ERP 연동 구성도 (제작 예정)", "file": None}],
        "glance": {"role": "백엔드 개발", "period": "2024.04 – 2024.10",
                   "stack": ["Java", "Spring", "ERP 연동"], "key_result": "ERP 연동 반복업무 40% 절감"},
        "problem": "", "decisions": [], "build": [], "result": {"metrics": [], "retro": ""},
    },
    {
        "id": "cs3", "slug": "cos", "code": "CS3", "accent": "amber",
        "name": "B2B 유전체 주문·정산 관리 (COS)",
        "period": "2024.03 ~ 2024.06",
        "card_one_liner": "주문·결제 백오피스 — State Machine 기반 정합성",
        "card_stack": ["Java", "Spring", "결제·정산"],
        "status": "skeleton",
        "hero": {"kicker": "CASE STUDY · CS3 · 2024.03–2024.06",
                 "title": "B2B 유전체 주문·정산 관리 (COS)", "sub": "랩지노믹스 IT팀"},
        "figures": [{"cap": "FIG.A — 주문 → 결제 → 정산 플로우 (제작 예정)", "file": None}],
        "glance": {"role": "백엔드 개발", "period": "2024.03 – 2024.06",
                   "stack": ["Java", "Spring", "결제·정산"], "key_result": "주문·결제 처리시간 30% 단축"},
        "problem": "", "decisions": [], "build": [], "result": {"metrics": [], "retro": ""},
    },
    {
        "id": "cs4", "slug": "ib", "code": "CS4", "accent": "coral",
        "name": "B2C 개인 맞춤 영양제 추천 (IB)",
        "period": "2022.08 ~ 2023.07",
        "card_one_liner": "PHR·유전자 기반 추천 플랫폼 신규 구축, KCP 결제",
        "card_stack": ["PHP", "MySQL", "KCP", "ClipSoft"],
        "status": "skeleton",
        "hero": {"kicker": "CASE STUDY · CS4 · 2022.08–2023.07",
                 "title": "B2C 개인 맞춤 영양제 추천 (IB)", "sub": "제노코어비에스 AI분석개발팀"},
        "figures": [],
        "glance": {"role": "백엔드 개발", "period": "2022.08 – 2023.07",
                   "stack": ["PHP", "MySQL", "KCP", "ClipSoft"], "key_result": "개인화 추천·KCP 결제 연동"},
        "problem": "", "decisions": [], "build": [], "result": {"metrics": [], "retro": ""},
    },
    {
        "id": "cs5", "slug": "aws", "code": "CS5", "accent": "purple",
        "name": "온프레미스 → AWS 전환",
        "period": "2024.01 ~ 진행 중",
        "card_one_liner": "이중화 설계·전환 — 비용 절감, 가용성 향상",
        "card_stack": ["AWS", "Nginx", "Podman", "Redis"],
        "status": "skeleton",
        "hero": {"kicker": "CASE STUDY · CS5 · 2024.01–진행 중",
                 "title": "온프레미스 → AWS 아키텍처 전환", "sub": "랩지노믹스 IT팀"},
        "figures": [
            {"cap": "FIG.A — Before / After 인프라 (제작 예정)", "file": None},
            {"cap": "FIG.B — 배포 · 장애 조치 플로우 (제작 예정)", "file": None},
        ],
        "glance": {"role": "아키텍처 설계·전환", "period": "2024.01 – 진행 중",
                   "stack": ["AWS (EC2·S3·ELB)", "Nginx", "Podman", "Redis"],
                   "key_result": "인프라 비용 46% 절감, 가용성 99.9% 이상"},
        "problem": "", "decisions": [], "build": [], "result": {"metrics": [], "retro": ""},
    },
]
