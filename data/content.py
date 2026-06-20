# -*- coding: utf-8 -*-
"""
포트폴리오 콘텐츠 단일 소스 (Single Source of Truth).

모든 페이지(홈·케이스 스터디)는 이 모듈에서만 데이터를 읽는다.
원본: 손준혁_이력서.md. CS2~CS5 본문은 이력서 작성 진행에 맞춰 채운다.

국/영 이중언어: 번역 대상 문자열은 L(ko, en)로 감싼다.
- 빌드 시 build.py의 t() 필터가 L → <span class="i ko">…</span><span class="i en">…</span>로 렌더한다.
- 기술 용어 등 언어 공통 문자열은 평문(str)으로 두면 t()가 그대로 통과시킨다(양 언어에 동일 노출).
- 리스트(스킬/스택 등)는 항목별로 평문/L을 섞어도 되고, 템플릿이 항목마다 t()를 적용한다.
"""


def L(ko, en):
    """이중 언어 문자열 — 템플릿에서 t() 필터로 렌더."""
    return {"ko": ko, "en": en}


SITE = {
    "name": L("손준혁", "JoonHyuk Son"),
    "role": L("백엔드 개발자 · 데이터 흐름 설계", "Backend Engineer · Data Flow Design"),
    "kicker": "BACKEND ENGINEER · DATA FLOW DESIGN",
    "bio_line": L("랩지노믹스 IT팀 선임 · 백엔드 개발", "Senior Backend Engineer · Labgenomics IT"),
    "positioning": L(
        "장비 연동, 주문·결제 트랜잭션, ERP, 인프라까지 — 도메인이 달라도 본질은 하나, "
        "데이터가 안정적으로 흐르는 구조를 설계합니다. 증상이 아니라 원인을 추적하는 방식으로 "
        "시스템을 만듭니다.",
        "Instruments, payment transactions, ERP, infrastructure — the domain changes, the "
        "essence does not: I design systems where data flows reliably, and I build them by "
        "tracing the cause rather than the symptom.",
    ),
    "work_intro": L(
        "장비 연동부터 B2B·B2C 서비스, 그 아래 인프라까지 5개 프로젝트입니다. "
        "도메인은 달라도 데이터 흐름과 상태를 안전하게 설계한다는 본질은 같습니다 — "
        "각 카드를 열면 케이스 스터디로 이어집니다.",
        "Five projects, from instrument integration to B2B and B2C services and the "
        "infrastructure beneath them. The domains differ, but the essence is the same — "
        "keeping data flow and state safe and consistent. Open each card for the case study.",
    ),
    "contacts": {
        "email": "zlfm48@gmail.com",
        "github": "github.com/nosnooj",
        "github_url": "https://github.com/nosnooj",
        "site": "nosnooj.github.io",
        "site_url": "https://nosnooj.github.io",
    },
    "profile_photo": "assets/img/profile.jpg",   # 증명사진 360x480(3:4)
    # 표지 대표 정량 성과 — 이력서 SUMMARY 대표 성과와 동일 4종(0건·70%·46%·99.9%).
    "metrics": [
        {"value": L("0건", "0"), "label": L("데이터 이관 오류", "Data-migration errors")},
        {"value": "70%↓", "label": L("ERP 월 결산 처리", "ERP monthly close")},
        {"value": "46%↓", "label": L("AWS 인프라 비용", "AWS infrastructure cost")},
        {"value": "99.9%+", "label": L("서비스 가용성", "Service availability")},
    ],
    "about": {
        "lede": L(
            "데이터를 분석하던 사람에서, 데이터가 안전하게 흐르는 시스템을 만드는 백엔드 개발자가 "
            "됐습니다. 통계학 석사를 마치고 미국 애드테크 기업에서 수백만 건의 광고·정산 데이터를 "
            "다루며 커리어를 시작해, 이후 유전체·헬스케어 IT로 옮겨 분석가에서 개발자로 전환했습니다. "
            "지금은 유전자 분석 장비 연동 LIMS, LIS–ERP 매출 연동, 온프레미스의 AWS 전환까지 "
            "백엔드 전 구간을 설계·구축·운영합니다. 데이터가 어디서 쌓여 어떻게 흐르는지를 먼저 보고 "
            "상태와 정합성을 명시적으로 설계하며, 문제가 생기면 증상이 아니라 원인을 추적하는 편입니다.",
            "I moved from analyzing data to building the systems that carry it. After a "
            "master's in statistics, I started my career handling millions of advertising and "
            "settlement records at a U.S. ad-tech company, then moved into genomics and "
            "healthcare IT, shifting from analyst to engineer. Today I design, build, and "
            "operate the full backend — an instrument-integrated LIMS, LIS–ERP revenue "
            "integration, and an on-prem-to-AWS migration. I look first at where data "
            "accumulates and how it flows, design state and consistency explicitly, and trace "
            "the cause rather than the symptom when something breaks.",
        ),
        "aspiration": L(
            "앞으로도 도메인을 가리지 않고, 데이터가 정확하고 안정적으로 흐르는 시스템을 설계하는 일을 "
            "이어가고 싶습니다. 분석으로 출발한 시야를 살려, 흐름과 근본 원인까지 설명할 수 있는 "
            "백엔드 엔지니어를 지향합니다.",
            "I want to keep designing systems where data flows accurately and reliably, "
            "whatever the domain. Drawing on a perspective that began in analysis, I aim to be "
            "a backend engineer who can explain both the flow and its root cause.",
        ),
        "career": [
            {
                "period": L("2023.12 ~ 재직 중", "Dec 2023 – Present"),
                "company": L("(주)랩지노믹스", "Labgenomics"),
                "role": L("선임 · IT팀 · 백엔드 개발", "Senior Backend Engineer · IT Team"),
                "scope": L(
                    "유전자 분석 LIMS · LIS–ERP 연동 · AWS 인프라 등 사내 핵심 백엔드 시스템의 "
                    "설계 · 구축 · 운영 전반 담당",
                    "Design, build, and operate core in-house backend systems — genomic-analysis "
                    "LIMS, LIS–ERP integration, and AWS infrastructure",
                ),
                "points": [
                    L("유전자 분석 장비 연동 Microarray LIMS(GAIA) 신규 구축 — 대용량 실험 데이터 수집·이관 "
                      "자동화로 데이터 동기화 오류 현재까지 0건",
                      "Built the instrument-integrated Microarray LIMS (GAIA) from scratch — "
                      "automated collection and migration of large experiment files, with 0 "
                      "data-sync errors to date"),
                    L("GAIA 결과지 생성·검사 모니터링 자동화 — 결과지 다운로드 시간 추정 95% 단축",
                      "Automated GAIA report generation and test monitoring — an estimated 95% "
                      "reduction in report download time"),
                    L("LIS–ERP10 매출 연동 플랫폼(LESS) 구축 — 수작업 월 결산 처리 약 70% 단축",
                      "Built the LIS–ERP10 revenue integration platform (LESS) — manual monthly "
                      "close reduced by ~70%"),
                    L("온프레미스 → AWS 아키텍처 전환 주도 — 인프라 비용 46% 절감, 가용성 99.9% 이상 확보",
                      "Led the on-prem → AWS migration — ~46% lower infrastructure cost and "
                      "99.9%+ availability"),
                    L("주문·정산 백오피스(COS) 구축 및 운영 웹·사내 LIMS 전반 유지보수 — 운영 이슈 100여 건 대응",
                      "Built the order/settlement back office (COS) and maintained the "
                      "operational web and in-house LIMS — resolved 100+ operational issues"),
                ],
            },
            {
                "period": L("2022.02 ~ 2023.11", "Feb 2022 – Nov 2023"),
                "company": L("(주)제노코어비에스", "Genocore BS"),
                "role": L("주임 · AI분석개발팀 · 백엔드 개발",
                          "Associate Backend Engineer · AI Analytics & Development Team"),
                "scope": L(
                    "B2C 헬스케어 서비스의 외부 데이터 API 연동 · 결제 · 백오피스 · 리포트 자동화 백엔드 개발",
                    "Backend development for a B2C healthcare service — external data API "
                    "integration, payments, back office, and report automation",
                ),
                "points": [
                    L("PHR·유전자 데이터 기반 B2C 영양제 추천·보험 상담 연계 플랫폼(IB) 구축 — 개인화 추천 "
                      "알고리즘 및 KCP 결제 연동",
                      "Built a B2C supplement-recommendation and insurance-consultation platform "
                      "(IB) on PHR and genetic data — a personalized recommendation algorithm and "
                      "KCP payment integration"),
                    L("ClipSoft Report 기반 결과지 자동화 — 양식 변경을 코드 배포 없이 반영하도록 "
                      "템플릿·데이터 매핑 계층 분리",
                      "Automated reports with ClipSoft Report — separated the template and "
                      "data-mapping layers so form changes ship without a code deploy"),
                ],
            },
            {
                "period": L("2018.06 ~ 2022.04", "Jun 2018 – Apr 2022"),
                "company": "Epsilon Data Management, LLC",
                "role": "Contractor · Technology Team",
                "scope": L(
                    "미국 애드테크 기업의 광고·정산 데이터 운영 자동화 및 대용량 데이터 분석 (한국 원격 근무)",
                    "Operations automation and large-scale data analysis for a U.S. ad-tech "
                    "company (remote from Korea)",
                ),
                "points": [
                    L("수백만 건 광고 데이터의 익월 예산 산정·100여 개 계정 Invoice 생성을 "
                      "Excel·VBA + Python 크롤링·캡처로 반자동화 — 반복 업무 시간 대폭 단축",
                      "Semi-automated next-month budget estimation across millions of ad records "
                      "and invoice generation for 100+ accounts using Excel · VBA + Python "
                      "crawling/capture — sharply cutting repetitive work"),
                    L("광고 플랫폼 운영 이슈를 Oracle SQL 대용량 데이터 분석으로 원인 규명·해결",
                      "Diagnosed and resolved ad-platform operational issues through large-scale "
                      "Oracle SQL analysis"),
                ],
            },
        ],
        "skills": [
            {"label": "Language", "items": ["Java", "Python", "PHP", "JavaScript", "SQL"]},
            {"label": "Backend", "items": ["Spring Boot", "Spring Security", "Spring AOP",
                                            "Spring WebFlux", "MyBatis", "JPA", "MQTT", "WebSocket",
                                            "CompletableFuture", "Thymeleaf", "FastAPI"]},
            {"label": "Database", "items": ["MS SQL Server", "MySQL", "Oracle"]},
            {"label": "Infra · DevOps", "items": ["AWS (EC2·VPC·NLB)", "Linux", "Nginx",
                                                   "Redis", "NFS", "Podman", "Docker",
                                                   "CI/CD (GitHub Actions·rsync)"]},
            {"label": L("기타", "Other"),
             "items": ["Azure OAuth2 SSO", L("KCP 결제 연동", "KCP payment"), "ClipSoft", "Git/GitHub"]},
        ],
        "education": [
            {
                "period": "2019.03 ~ 2021.02",
                "title": L("고려대학교 세종캠퍼스 · 응용통계학 석사",
                           "Korea University, Sejong Campus · M.S. in Applied Statistics"),
                "detail": L("학점 4.35 / 4.5 · 논문 «Bayesian inference for hidden stage "
                            "with distributed time delay»",
                            "GPA 4.35 / 4.5 · Thesis «Bayesian inference for hidden stage "
                            "with distributed time delay»"),
            },
            {
                "period": "2011.03 ~ 2017.02",
                "title": L("대구대학교 · 전산통계학과 학사 (복수전공: 경영학과)",
                           "Daegu University · B.S. in Computational Statistics "
                           "(double major: Business Administration)"),
                "detail": L("학점 4.1 / 4.5", "GPA 4.1 / 4.5"),
            },
        ],
        "certs": [
            {"date": "2024.09", "title": "TOEIC 935", "meta": "LC 495 / RC 440"},
            {"date": "2016.08", "title": "SAS Certified Predictive Modeler Using SAS Enterprise Miner 13",
             "meta": "SAS Institute · PMEM000721v13"},
            {"date": "2016.07", "title": "SAS Certified Advanced Programmer for SAS 9",
             "meta": "SAS Institute · AP017864v9"},
            {"date": "2015.07", "title": "SAS Certified Base Programmer for SAS 9",
             "meta": "SAS Institute · BP050880v9"},
            {"date": "2015.02", "title": "SAS Certified Statistical Business Analyst Using SAS 9",
             "meta": "SAS Institute · SBARM001510v9"},
        ],
        "etc": [
            {"date": "2017.01 ~ 2018.06",
             "title": L("한미 대학생 연수(WEST) 프로그램 · 국립국제교육원 선발",
                        "WEST Program (U.S.–Korea) · selected by the National Institute for "
                        "International Education"),
             "detail": L("POLY Languages Institute 어학 과정 수료 후 SearchForce, Inc.(San Mateo, CA) "
                         "기술서비스팀 인턴. 인턴십 성과로 정규 채용 제안, 이후 Epsilon 원격 Contractor 근속",
                         "Completed language training at POLY Languages Institute, then interned "
                         "on the Technical Services team at SearchForce, Inc. (San Mateo, CA). "
                         "Received a full-time offer based on internship performance, and "
                         "continued as a remote contractor at Epsilon.")},
            {"date": "2014.11", "title": L("2014학년도 제2학기 영어능력경시대회 10위",
                                           "English Proficiency Competition — 10th place "
                                           "(2014, 2nd semester)"),
             "detail": L("대구대학교 외국어교육센터", "Foreign Language Education Center, Daegu University")},
            {"date": "2012.08", "title": L("제6기 창의적 학습공동체 대상",
                                           "Grand Prize, Creative Learning Community (6th cohort)"),
             "detail": L("대구대학교 교무처 교육개발센터",
                         "Center for Educational Development, Daegu University")},
            {"date": "2012.07 ~ 2014.04",
             "title": L("병역 · 육군 병장 만기전역",
                        "Military Service · Republic of Korea Army, Sergeant (honorable completion)"),
             "detail": ""},
        ],
    },
}


# ---------------------------------------------------------------------------
# 프로젝트 (케이스 스터디)
# ---------------------------------------------------------------------------
PROJECTS = [
    {
        "id": "cs1",
        "slug": "gaia",
        "code": "CS1",
        "accent": "teal",
        "name": L("Microarray LIMS · 결과지·모니터링 자동화 (GAIA)",
                  "Microarray LIMS · Reporting & Monitoring Automation (GAIA)"),
        "period": "2024.07 ~ 2025.09",
        "card_one_liner": L("장비 연동부터 결과지 생성까지 단일 시스템화 — 이관 오류 0건",
                            "Instrument integration to report generation in one system — "
                            "0 migration errors"),
        "card_stack": ["Java", "Spring", "MQTT", "WebSocket"],
        "hero": {
            "kicker": "CASE STUDY · CS1 · 2024.07–2025.09",
            "title": L("장비에서 결과지까지, 손이 닿지 않는 흐름",
                       "From instrument to report — a flow no hand has to touch"),
            "sub": L("랩지노믹스 IT팀 · Microarray LIMS 신규 구축",
                     "Labgenomics IT Team · greenfield Microarray LIMS"),
        },
        "figures": [
            {"cap": L("FIG.A — 시스템 아키텍처", "FIG.A — System architecture"),
             "file": "gaia_arch.svg", "file_en": "gaia_arch.en.svg"},
        ],
        "glance": {
            "role": L("팀장과 전체 설계 주도 · 수집·이관·판독·LIS 연동·결과지/모니터링 웹 개발",
                      "Co-led the overall design with the team lead · built collection, "
                      "migration, interpretation, LIS integration, and the reporting/monitoring web"),
            "period": "2024.07 – 2025.09",
            "stack": ["Java", "Spring Boot", "Spring Security", "MQTT", "WebSocket",
                      "CompletableFuture", "Azure OAuth2", "AOP", "Thymeleaf", "MySQL",
                      "MS SQL Server", "Crownix Report(ClipSoft)"],
            "key_result": L("수작업 파일 이관·점검 제거, 데이터 이관 오류 0건",
                            "Eliminated manual file migration and checking — 0 data-migration errors"),
        },
        "problem": L(
            "유전자 검사 장비를 새로 도입하면서 그 데이터를 다룰 LIMS를 처음부터 설계·구축한 "
            "프로젝트입니다. 핵심 목표는 사람의 개입을 최소화하면서 처리 효율을 높이는 프로세스 "
            "자동화였습니다. 그래서 개발에 앞서, 운영에서 수작업에 의존하게 될 지점들을 풀어야 할 "
            "과제로 정리했습니다. 첫째, 장비가 만들어 내는 대용량 결과 파일을 실험실 담당자가 분석 "
            "서버로 직접 옮기고 이상 여부를 일일이 확인해야 했습니다. 둘째, 한 검체의 분석은 단계마다 "
            "짧게는 10분에서 길게는 3시간까지 걸리는 다단계 작업이라, 이를 안정적으로 실행·관리할 "
            "방법이 필요했습니다. 셋째, 기존 LIS에서는 결과지를 한 건씩만 내려받을 수 있어, 여러 검체를 "
            "한 번에 출력하려면 일괄(다건) 다운로드를 새로 지원해야 했습니다.",
            "This was a greenfield project: a new genetic-testing instrument was being "
            "introduced, and I designed and built the LIMS to handle its data from scratch. The "
            "core goal was process automation — raising throughput while keeping human "
            "intervention to a minimum. So before development, I mapped out the points that would "
            "otherwise depend on manual work as problems to solve. First, lab staff had to move "
            "the large result files the instrument produced to the analysis server by hand and "
            "check each one for anomalies. Second, analyzing a single sample was a multi-stage "
            "job taking from 10 minutes to 3 hours per stage, so it needed a reliable way to run "
            "and manage. Third, the existing LIS could download reports only one at a time, so "
            "printing many samples at once required new batch (multi-record) download.",
        ),
        "decisions": [
            {"head": L("상태와 대용량 전송을 분리한다", "Separate status from large-file transfer"),
             "body": L("실시간 진행률·오류 같은 가벼운 상태는 MQTT publish/subscribe로 구독·수집하고, "
                       "수백 MB~수 GB 결과 파일은 Socket 통신(TCP Socket·WebSocket)으로 분석 서버에 전송합니다 "
                       "— 폐쇄망 안에서 고속 송수신에 유리하기 때문입니다. "
                       "전송은 CompletableFuture로 병렬화해 다수 파일을 동시에 처리합니다.",
                       "Lightweight status such as real-time progress and errors is collected over "
                       "MQTT publish/subscribe, while result files of hundreds of MB to several GB "
                       "are sent to the analysis server over socket communication (TCP socket / "
                       "WebSocket) — well suited to fast transfer within a closed network. "
                       "Transfers are parallelized with CompletableFuture to handle many files at once.")},
            {"head": L("분석 진행을 명시적 State Machine으로 고정한다",
                       "Pin analysis progress to an explicit state machine"),
             "body": L("Run 상태를 QUEUED → RUNNING → COMPLETED / FAILED / RETRY로 명시 정의하고 "
                       "비정상 전이를 차단합니다. 제한된 서버 자원 안에서 스레드 풀로 작업을 스케줄링합니다.",
                       "Run state is explicitly defined as QUEUED → RUNNING → COMPLETED / FAILED / "
                       "RETRY, blocking invalid transitions. Jobs are scheduled with a thread pool "
                       "within limited server resources.")},
            {"head": L("내부망과 외부 공유 영역을 물리적으로 나눈다",
                       "Physically separate the internal network from the externally shared zone"),
             "body": L("분석 서버(LIMS 코어)는 내부망 전용, 결과지 생성·다운로드·검사 모니터링 웹은 "
                       "외부 공유 웹 호스팅 서버(DMZ)로 분리해 의뢰기관·외부 사용자 접근 경로를 격리합니다.",
                       "The analysis server (LIMS core) stays internal-only, while the web for "
                       "report generation, download, and test monitoring is split onto an "
                       "externally shared hosting server (DMZ), isolating access paths for "
                       "client institutions and external users.")},
        ],
        "build": [
            {"module": L("장비 상태 실시간 수집 · 대용량 결과 이관",
                         "Real-time instrument status · large-result migration"),
             "points": [
                 L("MQTT(Subscribe/Publish)로 장비 Run 상태(진행률·오류)를 실시간 구독·수집해 모니터링에 반영",
                   "Subscribed to and collected instrument Run status (progress, errors) in real "
                   "time over MQTT (subscribe/publish) and surfaced it in monitoring"),
                 L("Run 종료 시 대용량 결과 파일을 Socket 통신(TCP Socket·WebSocket)으로 분석 서버에 전송 "
                   "— 폐쇄망 고속 전송 활용, CompletableFuture 병렬 전송으로 다수 파일을 동시 처리해 이관 시간을 평균 25~30분에서 약 5분으로 단축",
                   "On Run completion, sent large result files to the analysis server over socket "
                   "communication (TCP socket / WebSocket) — using fast closed-network transfer and "
                   "parallel sends via CompletableFuture to handle many files at once, cutting "
                   "migration time from an average of 25–30 minutes to about 5"),
                 L("이관 과정의 중복·충돌·경로 오류를 유형별로 방어해 운영 후 현재까지 이관 오류 0건",
                   "Guarded against duplication, collision, and path errors by type during "
                   "migration — 0 migration errors since go-live to date"),
             ]},
            {"module": L("분석 파이프라인 작업 오케스트레이션",
                         "Analysis-pipeline job orchestration"),
             "points": [
                 L("이관된 샘플이 다단계 파이프라인(단계별 10분~3시간)을 자동 수행하도록 작업 관리·모니터링 체계 설계",
                   "Designed job management and monitoring so migrated samples run a multi-stage "
                   "pipeline (10 minutes to 3 hours per stage) automatically"),
                 L("제한된 서버 자원 내 스레드 풀 병렬 처리로 분석 작업 스케줄링",
                   "Scheduled analysis jobs with thread-pool parallelism within limited server resources"),
                 L("Run 상태를 명시적 State(QUEUED→RUNNING→COMPLETED/FAILED/RETRY)로 정의해 비정상 전이 차단",
                   "Defined Run state explicitly (QUEUED→RUNNING→COMPLETED/FAILED/RETRY) to block "
                   "invalid transitions"),
             ]},
            {"module": L("결과 판독 웹 · 수진자 매핑 · LIS 양방향 연동",
                         "Result-interpretation web · patient mapping · bidirectional LIS integration"),
             "points": [
                 L("파이프라인 산출물을 DB 적재 후, 분석자가 수치형·이미지 데이터를 판독·입력·메모하는 "
                   "결과 판독 웹 구축(Audit·로그 포함)",
                   "After loading pipeline outputs into the DB, built a result-interpretation web "
                   "where analysts read, enter, and annotate numeric and image data (with audit and logging)"),
                 L("수진자 매핑 데몬 개발 — 수진자 ID만 매핑하면 LIS에서 정보를 자동 조회·연계(LIMS/LIS DB 분리 운영)",
                   "Built a patient-mapping daemon — mapping just a patient ID automatically looks up and "
                   "links information from the LIS (LIMS and LIS DBs run separately)"),
                 L("판독 완료 결과를 LIS로 연동하는 데몬을 구축해, 장비에서 판독을 거쳐 LIS까지 이어지는 "
                   "흐름을 양방향으로 자동 연계, 시스템 간 이중 입력·수작업 매핑 제거",
                   "Built a daemon that pushes finalized interpretations to the LIS, linking the "
                   "flow from instrument through interpretation to LIS bidirectionally and removing "
                   "double entry and manual mapping between systems"),
             ]},
            {"module": L("결과지 자동 생성 데몬 · 다운로드 · 검사 모니터링",
                         "Report auto-generation daemon · download · test monitoring"),
             "points": [
                 L("Crownix Report(ClipSoft)로 최종 처리된 샘플 결과지를 매시간 자동 생성하는 스케줄 데몬 구축",
                   "Built a scheduled daemon that auto-generates reports for finalized samples "
                   "hourly with Crownix Report (ClipSoft)"),
                 L("수진자 정보 변경·결과 재입력 시 API 호출로 해당 결과지만 선별 재생성",
                   "On patient-info changes or re-entered results, regenerated only the affected "
                   "reports via an API call"),
                 L("기존 LIS는 결과지를 건별로만 내려받을 수 있던 것을 일괄(다건) 다운로드로 확장하고 "
                   "audit·이력 관리를 추가해 결과지 다운로드 시간 추정 약 95% 단축",
                   "Extended the existing LIS — which could download reports only one at a time — "
                   "to batch (multi-record) download and added audit and history management, "
                   "cutting report download time by an estimated ~95%"),
                 L("재채혈 요청·검사취소·고위험군·양성 판정 등 특이 소견을 한 화면에서 즉시 식별하는 모니터링 페이지 구축",
                   "Built a monitoring page that surfaces notable findings — re-draw requests, "
                   "cancellations, high-risk groups, positive results — at a glance on one screen"),
             ]},
            {"module": L("공통 기반", "Common foundation"),
             "points": [
                 L("Azure OAuth2 SSO · 메뉴 ACL로 접근 제어",
                   "Access control via Azure OAuth2 SSO and menu-level ACL"),
                 L("AOP Audit 로깅으로 QA 감사 추적",
                   "QA audit trail through AOP audit logging"),
                 L("GlobalExceptionHandler · BusinessException으로 예외 처리 일원화",
                   "Unified exception handling with GlobalExceptionHandler and BusinessException"),
             ]},
        ],
        "result": {
            "metrics": [
                {"value": L("0건", "0"), "label": L("데이터 이관 오류", "Data-migration errors")},
                {"value": L("25~30→5분", "25–30 → 5 min"),
                 "label": L("대용량 결과 이관", "Large-result migration")},
                {"value": L("약 95%↓", "~95%↓"),
                 "label": L("결과지 일괄 다운로드", "Batch report download")},
                {"value": L("즉시 식별", "At a glance"),
                 "label": L("특이 소견", "Notable findings")},
            ],
            "retro": L("운영에서 사람 손이 닿을 지점을 개발 전에 미리 과제로 정의해 둔 덕에, "
                       "출시 후에는 별도 개입 없이 흐름이 돌아갑니다.",
                       "Because I defined the spots where operations would still need a human touch "
                       "as problems before development, the flow runs after launch without extra intervention."),
        },
    },
    {
        "id": "cs2", "slug": "less", "code": "CS2", "accent": "blue",
        "name": L("LIS–ERP 연동 웹플랫폼 (LESS)", "LIS–ERP Integration Platform (LESS)"),
        "period": "2024.04 ~ 2024.10",
        "card_one_liner": L("검사–회계 데이터 흐름 연동 — 월 결산 약 70% 단축",
                            "Linking lab-test and accounting data — monthly close ~70% faster"),
        "card_stack": ["Java", "Spring", "WebFlux", L("ERP 연동", "ERP integration")],
        "hero": {
            "kicker": "CASE STUDY · CS2 · 2024.04–2024.10",
            "title": L("검사 매출에서 ERP까지, 손으로 맞추지 않는 결산",
                       "From lab-test revenue to ERP — a close not reconciled by hand"),
            "sub": L("랩지노믹스 IT팀 · LIS–ERP10 매출 연동 플랫폼",
                     "Labgenomics IT Team · LIS–ERP10 revenue integration platform"),
        },
        "figures": [
            {"cap": L("FIG.A — 시스템 아키텍처", "FIG.A — System architecture"),
             "file": "less_arch.svg", "file_en": "less_arch.en.svg"},
        ],
        "build_fig": {"cap": L("FIG.B — 월 결산 연동 플로우 (연동관리자 월별 프로세스)",
                               "FIG.B — Monthly close integration flow (integration manager's monthly process)"),
                      "file": "less_flow.svg", "file_en": "less_flow.en.svg"},
        "glance": {
            "role": L("3인 팀(팀원) · 담당 검사·매출 분야 풀스택 구현 · 전체 아키텍처 팀 공동 설계",
                      "3-person team (member) · full-stack build of my assigned test/revenue "
                      "domains · co-designed the overall architecture"),
            "period": "2024.04 – 2024.10",
            "stack": ["Java", "Spring Boot", "Spring WebFlux", "Spring Security", "MyBatis",
                      "WebClient", "Strategy Pattern", "Multi-DataSource", "MySQL",
                      "MS SQL Server", "Thymeleaf", "Apache POI"],
            "key_result": L("수작업 월 결산을 자동화, 처리 시간 약 70% 단축",
                            "Automated the manual monthly close, cutting processing time by ~70%"),
        },
        "problem": L(
            "전사 ERP10 도입에 맞춰, 자사 LIS에 쌓이는 매출 데이터를 ERP10 연동 규격으로 가공해 "
            "전송하는 체계가 필요했습니다. 매출은 수백 종 검사와 수백 개 거래처에 영업소·대리점·해외 "
            "매출, 무료검사 회계처리까지 얽혀 있어 매월 결산 때 정확한 집계 자체가 일이었고, 실무진이 "
            "수작업으로 며칠을 들였습니다. 분야마다 정산 규칙이 다르고, 원천인 LIS와 "
            "ERP10은 데이터 규격·통신 방식이 달라, 데이터 정합성을 지키면서 이 차이를 흡수하는 구조가 "
            "과제였습니다.",
            "Alongside a company-wide ERP10 rollout, we needed a system to transform the revenue "
            "data accumulating in our LIS into the ERP10 integration spec and transmit it. Revenue "
            "was tangled across hundreds of test types and hundreds of clients, with branch, "
            "agency, and overseas sales and the accounting of free tests, so accurate aggregation "
            "at each monthly close was itself a chore that took staff days by hand. Settlement "
            "rules differed by domain, and the source LIS and ERP10 used different data formats "
            "and communication methods, so the challenge was a structure that absorbed those "
            "differences while preserving data consistency.",
        ),
        "decisions": [
            {"head": L("검사·매출 분야별로 정산을 전략으로 나눈다",
                       "Split settlement into strategies by test/revenue domain"),
             "body": L("분야마다 다른 조회·정산 규칙을 하나의 분기문에 몰지 않고, BillingService 아래 "
                       "분야별 구현체(전략 패턴)로 분리했습니다. 팀원별 분담 개발과 새 매출 분야 확장을 "
                       "기존 코드 충돌 없이 가능하게 합니다.",
                       "Rather than cramming each domain's differing lookup and settlement rules "
                       "into one branch, I separated them into per-domain implementations (Strategy "
                       "pattern) under BillingService. This lets teammates divide work and lets new "
                       "revenue domains be added without conflicting with existing code.")},
            {"head": L("대량 연동은 WebFlux 논블로킹으로 일괄 처리한다",
                       "Batch large integrations with WebFlux non-blocking"),
             "body": L("결산 시점에 매출이 한꺼번에 몰리므로, Spring WebFlux·WebClient 논블로킹으로 "
                       "수주(SO)·생산지시를 일괄 전송합니다. 건마다 응답을 기다리는 블로킹 방식 대비 "
                       "대기 시간을 줄였습니다.",
                       "Because revenue arrives all at once at close, sales orders (SO) and "
                       "production orders are sent in batch via Spring WebFlux / WebClient "
                       "non-blocking, reducing wait time compared with blocking call-by-call.")},
            {"head": L("원천과 운영 데이터를 읽기/쓰기로 분리한다",
                       "Separate source and operational data into read/write"),
             "body": L("원천인 LIS(MSSQL)는 읽기 전용, 가공·연동 데이터는 운영 DB(MySQL)에 쓰도록 "
                       "MyBatis SqlSessionFactory를 데이터소스별로 분리해 원천 데이터 오염 위험을 "
                       "차단했습니다.",
                       "The source LIS (MSSQL) is read-only and processed/integration data is "
                       "written to the operational DB (MySQL); I split the MyBatis "
                       "SqlSessionFactory per data source to eliminate the risk of corrupting source data.")},
            {"head": L("연동을 건별 상태로 추적해 실패를 격리한다",
                       "Track integration per record to isolate failures"),
             "body": L("전송을 건별 성공/실패 상태로 기록하고, 실패한 건만 선별해 재연동할 수 있게 "
                       "했습니다. 일부 실패가 전체 마감을 막지 않도록 격리해 월 결산의 신뢰성을 "
                       "확보했습니다.",
                       "Each transmission is recorded with success/failure status so only failed "
                       "records can be reprocessed selectively. Isolating partial failures so they "
                       "don't block the whole close secured the reliability of the monthly close.")},
        ],
        "build": [
            {"module": L("매출 데이터 취합 · 조회 · 검증", "Revenue aggregation · lookup · validation"),
             "points": [
                 L("실무자 정산 프로세스에 맞춰 자사 LIS(MS SQL Server)에서 매출을 취합·조회·검증하는 "
                   "웹 화면을 백엔드부터 프런트엔드(Thymeleaf·jQuery·TUI Grid)까지 구현",
                   "Built web screens to aggregate, look up, and validate revenue from our LIS "
                   "(MS SQL Server) along the staff settlement process, from backend to frontend "
                   "(Thymeleaf · jQuery · TUI Grid)"),
                 L("검사·매출 분야별로 조회·정산 로직을 분리하는 전략 패턴 위에서 담당 분야 구현체를 "
                   "개발 — 분야별 분담 개발과 신규 분야 확장이 용이",
                   "Developed my domain's implementations on a Strategy pattern that separates "
                   "lookup/settlement logic by test/revenue domain — making divided development and "
                   "new-domain extension easy"),
                 L("무료조정금액 검증과 중복 방지(해당 월 데이터 삭제 후 재등록)로 결산 데이터 정확도 확보",
                   "Secured close-data accuracy with free-adjustment validation and "
                   "duplicate prevention (delete-then-re-register the month's data)"),
             ]},
            {"module": L("ERP10 연동 (수주 · 생산지시)", "ERP10 integration (sales & production orders)"),
             "points": [
                 L("검증된 매출을 ERP10 인터페이스로 전송 — LIS 독자 규격(CamelCase)을 ERP10 "
                   "규격(Snake_case)으로 변환하는 매핑 계층 적용",
                   "Sent validated revenue to the ERP10 interface — applying a mapping layer that "
                   "converts the LIS's own format (CamelCase) to the ERP10 format (Snake_case)"),
                 L("Spring WebFlux·WebClient 논블로킹으로 수주(SO)·생산지시 정보를 일괄 전송 "
                   "— 대량 매출 처리 시 블로킹 대비 지연 최소화",
                   "Sent sales-order (SO) and production-order data in batch via Spring WebFlux / "
                   "WebClient non-blocking — minimizing latency versus blocking on large volumes"),
                 L("RSA 암호화 토큰 인증·운영 환경 Proxy 연동으로 ERP10 API 보안 연동",
                   "Secured ERP10 API integration with RSA-encrypted token authentication and a "
                   "production proxy"),
             ]},
            {"module": L("연동 이력 관리 · 재처리", "Integration history · reprocessing"),
             "points": [
                 L("건별 연동 상태(성공/실패)와 에러 로그를 추적·저장하고, 실패 건만 선별 재연동하는 기능 구축",
                   "Tracked and stored per-record integration status (success/failure) and error "
                   "logs, with selective reprocessing of failed records"),
                 L("결산 매출 데이터를 Excel(Apache POI)로 추출",
                   "Exported close revenue data to Excel (Apache POI)"),
             ]},
            {"module": L("공통 기반", "Common foundation"),
             "points": [
                 L("다중 데이터소스 — 읽기 전용 LIS(MSSQL)와 쓰기 운영 DB(MySQL)를 MyBatis SqlSessionFactory로 분리",
                   "Multi-datasource — separated the read-only LIS (MSSQL) and the write "
                   "operational DB (MySQL) via MyBatis SqlSessionFactory"),
                 L("Spring Security 인증 · Argon2 해싱 · 역할 기반 접근제어",
                   "Spring Security authentication · Argon2 hashing · role-based access control"),
                 L("운영 환경 Redis 세션 · HikariCP 커넥션 풀",
                   "Redis sessions and the HikariCP connection pool in production"),
             ]},
        ],
        "result": {
            "metrics": [
                {"value": L("약 70%↓", "~70%↓"),
                 "label": L("월 결산 처리 시간 단축 (수일→수시간, 실무자 평가)",
                            "Monthly close time (days → hours, staff-assessed)")},
                {"value": L("수작업 → 자동", "Manual → automated"),
                 "label": L("월 매출 정산 수작업 제거 — 실무진은 검증에 집중",
                            "Removed manual monthly settlement — staff focus on validation")},
            ],
            "retro": L("검사 분야마다 다른 정산 규칙을 전략으로 나누고 실패 건을 격리해 둔 덕에, "
                       "며칠씩 손으로 맞추던 월 결산을 시스템이 대신 돌리고 실무진은 검증에 집중하게 됐습니다.",
                       "Because I split each test domain's settlement rules into strategies and "
                       "isolated failures, the system now runs the monthly close that once took "
                       "days by hand, and staff focus on validation."),
        },
    },
    {
        "id": "cs3", "slug": "aws", "code": "CS3", "accent": "amber",
        "name": L("온프레미스 → AWS 아키텍처 전환", "On-prem → AWS Architecture Migration"),
        "period": "2024.01 ~ 2024.06",
        "card_one_liner": L("단일 서버에서 다중 AZ 이중화로 — 비용 46%↓, 가용성 99.9%↑",
                            "From a single server to multi-AZ redundancy — cost 46%↓, "
                            "availability 99.9%↑"),
        "card_stack": ["AWS VPC", "Nginx ARR", "Podman", "NFS·Redis"],
        "hero": {
            "kicker": "CASE STUDY · CS3 · 2024.01–2024.06",
            "title": L("한 대가 멈춰도, 멈추지 않는 인프라",
                       "One node stops, the infrastructure doesn't"),
            "sub": L("랩지노믹스 IT팀 · 온프레미스 → AWS VPC 다중 AZ 전환",
                     "Labgenomics IT Team · on-prem → AWS VPC multi-AZ migration"),
        },
        "figures": [
            {"cap": L("FIG.A — AWS VPC 다중 AZ 아키텍처", "FIG.A — AWS VPC multi-AZ architecture"),
             "file": "aws_arch.svg", "file_en": "aws_arch.en.svg"},
        ],
        "glance": {
            "role": L("전환 아키텍처 설계·구축 주도 · 네트워크·보안·이중화·스토리지 전 구간",
                      "Led the migration architecture design and build · network, security, "
                      "redundancy, and storage end to end"),
            "period": "2024.01 – 2024.06",
            "stack": ["AWS VPC", "EC2", "NLB", "NAT/IGW", "Nginx(ARR·HSTS)", "Podman",
                      "Redis", "NFS", "MariaDB", "rsync", "GitHub Actions"],
            "key_result": L("인프라 비용 약 46% 절감, 가용성 99.9% 이상",
                            "~46% lower infrastructure cost, 99.9%+ availability"),
        },
        "problem": L(
            "온프레미스에서 운영하던 외부 사용자 대상 웹 서비스(한국·미국 법인 홈페이지, 제품 "
            "브랜드 홈페이지, 거래처용 웹플랫폼 — 검사 접수·조회, 결과 조회·다운로드)는 단일 서버 "
            "의존과 수작업 운영에 묶여 있었습니다. 외부 사용자가 상시 접속하는 서비스라 한 노드만 "
            "멈춰도 접속이 끊겼고, 설정·배포가 사람 손에 달려 있었습니다. 핵심 과제는 셋이었습니다. "
            "첫째, 어느 한 노드가 멈춰도 서비스가 이어지는 이중화. 둘째, 외부에 운영 서버를 직접 노출하지 않는 "
            "보안 접근 경계. 셋째, 여러 노드가 같은 파일·세션·DB를 일관되게 바라보는 상태 공유 "
            "구조. 이를 AWS VPC 기반으로 재설계해 옮기는 것이 목표였습니다.",
            "An external-facing web service running on-premises (the Korean and U.S. corporate "
            "sites, product brand sites, and a client web platform — test intake/lookup and result "
            "lookup/download) was bound to a single server and manual operation. Because external "
            "users connect around the clock, one node going down cut off access, and configuration "
            "and deployment depended on people. There were three core tasks. First, redundancy so "
            "the service continues even if a node stops. Second, a security boundary that doesn't "
            "expose operational servers directly to the outside. Third, a shared-state structure "
            "where multiple nodes see the same files, sessions, and DB consistently. The goal was "
            "to re-architect this onto AWS VPC and migrate it.",
        ),
        "decisions": [
            {"head": L("퍼블릭/프라이빗을 다중 AZ로 나눈다", "Split public/private across multiple AZs"),
             "body": L("Nginx·Bastion만 퍼블릭 서브넷에 두고 WAS·DB·NFS·Redis는 프라이빗 서브넷으로 "
                       "내려, 운영 자원의 외부 노출을 없앴습니다. 서브넷을 여러 가용영역(AZ)에 분산해 "
                       "한 영역 장애가 전체로 번지지 않게 했습니다.",
                       "Only Nginx and Bastion sit in public subnets; WAS, DB, NFS, and Redis move "
                       "to private subnets, removing external exposure of operational resources. "
                       "Subnets are spread across availability zones (AZs) so a single-zone failure "
                       "doesn't cascade.")},
            {"head": L("리버스 프록시를 이중화해 단일 장애점을 없앤다",
                       "Make the reverse proxy redundant to remove the single point of failure"),
             "body": L("기존에는 한 대의 호스트가 리버스 프록시(ARR)를 전담해 단일 장애점이었습니다. "
                       "NLB 뒤에 Nginx ARR 노드를 두 대로 이중화하고 HSTS를 적용해, 한 대가 멈춰도 "
                       "트래픽이 다른 노드로 흐르게 했습니다.",
                       "Previously a single host handled the reverse proxy (ARR) — a single point "
                       "of failure. I made the Nginx ARR redundant with two nodes behind an NLB and "
                       "applied HSTS, so traffic flows to the other node if one stops.")},
            {"head": L("이중화된 설정은 자동 동기화로 일치시킨다",
                       "Keep redundant configs in sync automatically"),
             "body": L("이중화한 두 Nginx 노드의 설정이 어긋나면 그대로 장애가 되므로, rsync로 설정을 "
                       "노드 간 자동 동기화해 구성 불일치를 차단했습니다.",
                       "Since drift between the two Nginx nodes' configs would itself cause an "
                       "outage, I synced configs between nodes automatically with rsync to prevent "
                       "configuration mismatch.")},
            {"head": L("상태·파일을 분리해 무상태 웹을 만든다",
                       "Separate state and files to make the web stateless"),
             "body": L("세션은 Redis로, 이미지·업로드 같은 공통 파일은 저비용 EC2·EBS 기반 자체 NFS로 "
                       "빼내 여러 웹 노드가 같은 상태를 바라보게 했습니다. 웹 계층을 무상태로 만들어 "
                       "노드 추가·교체가 자유롭습니다.",
                       "Sessions moved to Redis and shared files such as images and uploads to a "
                       "self-hosted NFS on low-cost EC2/EBS, so multiple web nodes see the same "
                       "state. Making the web tier stateless makes adding or replacing nodes easy.")},
        ],
        "build": [
            {"module": L("VPC 네트워크 · 보안", "VPC network · security"),
             "points": [
                 L("다중 AZ에 퍼블릭(Nginx·Bastion)·프라이빗(WAS·DB·NFS·Redis) 서브넷 분리 설계",
                   "Designed public (Nginx, Bastion) and private (WAS, DB, NFS, Redis) subnets "
                   "separated across multiple AZs"),
                 L("Bastion Host 단일 SSH 경로로 접근 통제 — 온프레미스 IP만 허용, 내부·외부 경로 분리",
                   "Controlled access via a single SSH path through the Bastion host — allowing "
                   "only on-prem IPs and separating internal/external paths"),
                 L("NAT Gateway로 프라이빗 아웃바운드 분리, Internet Gateway는 퍼블릭 계층에만 연결",
                   "Separated private outbound with a NAT Gateway, attaching the Internet Gateway "
                   "to the public tier only"),
             ]},
            {"module": L("로드밸런싱 · 이중화 (가용성)", "Load balancing · redundancy (availability)"),
             "points": [
                 L("NLB 뒤 Nginx 리버스 프록시(ARR) 2노드 이중화 · HSTS 적용 — 단일 리버스 프록시(AS-IS)의 단일 장애점 제거(TO-BE)",
                   "Two-node Nginx reverse-proxy (ARR) redundancy behind an NLB with HSTS — "
                   "removing the single point of failure of the single reverse proxy (AS-IS → TO-BE)"),
                 L("웹 호스팅 노드(Podman 컨테이너)와 Java WAS를 다중 AZ에 분산·이중화",
                   "Distributed and made redundant the web-hosting nodes (Podman containers) and "
                   "Java WAS across multiple AZs"),
                 L("rsync로 Nginx 설정을 노드 간 자동 동기화해 구성 불일치 방지",
                   "Prevented configuration mismatch by auto-syncing Nginx configs between nodes with rsync"),
             ]},
            {"module": L("세션 · 공유 스토리지 · DB", "Sessions · shared storage · DB"),
             "points": [
                 L("Redis 세션 스토어로 다중 웹 노드 간 세션 공유(무상태 웹 계층)",
                   "Shared sessions across web nodes with a Redis session store (stateless web tier)"),
                 L("저비용 EC2·EBS 기반 자체 NFS로 이미지·업로드 파일 등 공통 파일을 전 노드에서 동일 접근",
                   "Gave all nodes the same access to shared files (images, uploads) via a "
                   "self-hosted NFS on low-cost EC2/EBS"),
                 L("MariaDB 프라이빗 서브넷 전용 인스턴스 운영",
                   "Ran MariaDB on a dedicated private-subnet instance"),
             ]},
            {"module": L("전환", "Migration"),
             "points": [
                 L("온프레미스 서비스를 무중단 기준으로 단계적 이관, 자원 구성 재설계로 비용 약 46% 절감",
                   "Migrated the on-prem service in phases with zero downtime and cut cost by ~46% "
                   "through resource redesign"),
                 L("단계적 전환·검증을 반복하며 가용성 99.9% 이상으로 안정화",
                   "Stabilized at 99.9%+ availability through repeated phased migration and validation"),
             ]},
        ],
        "result": {
            "metrics": [
                {"value": L("약 46%↓", "~46%↓"), "label": L("인프라 비용 절감", "Infrastructure cost")},
                {"value": "99.9%↑", "label": L("시스템 가용성 (단일 장애점 제거)",
                                                "System availability (SPOF removed)")},
                {"value": L("무중단 이관", "Zero-downtime"),
                 "label": L("온프레미스 서비스 단계적 전환", "Phased on-prem migration")},
                {"value": L("무상태 웹", "Stateless web"),
                 "label": L("세션·파일 분리로 수평 확장", "Horizontal scale via session/file split")},
            ],
            "retro": L("한 대가 멈춰도 서비스가 멈추지 않도록 이중화와 상태 분리를 먼저 설계한 덕에, "
                       "전환 후에는 노드를 더하고 빼는 일이 운영의 일부가 됐습니다.",
                       "Because I designed redundancy and state separation first so a stopped node "
                       "wouldn't stop the service, adding and removing nodes became part of routine "
                       "operations after the migration."),
        },
    },
    {
        "id": "cs4", "slug": "cos", "code": "CS4", "accent": "coral",
        "name": L("B2B 유전체 주문·정산 관리 (COS)", "B2B Genomics Order & Settlement (COS)"),
        "period": "2024.03 ~ 2024.06",
        "card_one_liner": L("엑셀 수작업 정산을 단일 백오피스로 — 잔액 검증·감사 추적",
                            "Excel-based settlement into one back office — balance checks, "
                            "audit trail"),
        "card_stack": ["Java", "Spring", L("PI 선불계정", "PI prepaid"), L("정산·회계", "Settlement")],
        "hero": {
            "kicker": "CASE STUDY · CS4 · 2024.03–2024.06",
            "title": L("주문에서 정산까지, 엑셀을 떠난 한 화면",
                       "From order to settlement — one screen, off the spreadsheet"),
            "sub": L("랩지노믹스 IT팀 · B2B 유전체 주문·정산 백오피스",
                     "Labgenomics IT Team · B2B genomics order & settlement back office"),
        },
        "figures": [
            {"cap": L("FIG.A — 주문 → 정산 데이터 플로우", "FIG.A — Order → settlement data flow"),
             "file": "cos_flow.svg", "file_en": "cos_flow.en.svg"},
        ],
        "glance": {
            "role": L("기획 2·개발 1의 3인 프로젝트 · 주문·정산·회계 백엔드·프런트엔드 단독 구현",
                      "3-person project (2 product, 1 dev) · sole developer of order, settlement, "
                      "and accounting (backend and frontend)"),
            "period": "2024.03 – 2024.06",
            "stack": ["Java", "Spring Boot", "MyBatis", "MS SQL Server", "Thymeleaf", "jQuery"],
            "key_result": L("엑셀 수작업 정산을 단일 백오피스로 일원화 · 모든 변경 감사 추적",
                            "Consolidated Excel-based settlement into one back office · full change "
                            "audit trail"),
        },
        "problem": L(
            "B2B 유전체 분석 사업은 주문부터 정산까지를 엑셀로 관리하고 있었습니다. 고객은 "
            "연구기관과 PI(연구책임자)이고, 이들이 미리 충전한 PI 선불계정 잔액에서 주문 금액을 "
            "차감하는 구조라 잔액·미수금·이체·환불 계산이 수기로 얽혔습니다. 견적·주문·샘플 이력은 흩어져 "
            "있었고, 결제·입금 내역과 회계기관 정산이 분리돼 있어 누가 언제 무엇을 바꿨는지 추적도 "
            "어려웠습니다. 흩어진 엑셀 업무를 한 시스템으로 모으고, 모든 변경을 감사 추적이 "
            "가능하게 만드는 것이 과제였습니다.",
            "The B2B genomics-analysis business managed everything from order to settlement in "
            "spreadsheets. Customers are research institutions and PIs (principal investigators), "
            "and because order amounts are deducted from a PI prepaid-account balance topped "
            "up in advance, the balance, receivables, transfer, and refund calculations were tangled "
            "by hand. Quote, order, and sample histories were scattered, and payment/deposit records "
            "were separate from accounting-institution settlement, so it was hard to trace who "
            "changed what and when. The task was to gather the scattered spreadsheet work into one "
            "system and make every change auditable.",
        ),
        "decisions": [
            {"head": L("거래처를 기관–PI–고객 마스터로 표준화한다",
                       "Standardize clients into an institution–PI–customer master"),
             "body": L("주문·정산의 기준이 되는 거래처 정보를 기관·PI·고객 마스터로 정규화하고 소속 "
                       "관계로 연결해, 엑셀마다 다르던 거래처 표기를 한 곳으로 모았습니다.",
                       "Normalized the client data underpinning orders and settlement into "
                       "institution, PI, and customer masters, linked by affiliation — consolidating "
                       "client labels that differed across spreadsheets into one place.")},
            {"head": L("PI 선불계정 잔액을 주문의 관문으로 둔다",
                       "Make the PI prepaid-account balance the gate for orders"),
             "body": L("주문 등록 시 PI 선불계정 잔액과 주문총액을 비교해, 잔액이 부족하면 경고로 "
                       "막았습니다. 회계기관계정에서 PI 계정으로 금액을 이동(충전)하는 경로와 PI 계정 간 "
                       "이체를 구분하고, 잔액·미수금을 함께 관리해 수기 계산 오류가 정산에 흘러드는 길을 "
                       "끊었습니다.",
                       "At order entry, compared the PI prepaid balance against the order total and "
                       "blocked with a warning on insufficient funds. Distinguished moving funds "
                       "(top-up) from the accounting-institution account to a PI account from "
                       "transfers between PI accounts, and managed balance and receivables together "
                       "— cutting off the path for manual calculation errors to flow into settlement.")},
            {"head": L("결제·입금은 취소·환불까지 정합을 맞춘다",
                       "Reconcile payments/deposits through cancellation and refund"),
             "body": L("결제·입금의 등록뿐 아니라 취소·환불까지 다루되, 취소·환불 시 회계기관계정의 "
                       "결제누적총액·입금총액을 되돌려 재정합했습니다. 정산 데이터가 어느 시점에도 맞도록 했습니다.",
                       "Handled not just registering payments and deposits but also cancellations "
                       "and refunds, reversing and reconciling the accounting-institution account's "
                       "cumulative payment and deposit totals on cancel/refund — keeping settlement "
                       "data correct at any point in time.")},
            {"head": L("모든 변경을 감사 추적으로 남긴다", "Leave every change in an audit trail"),
             "body": L("주문·정산은 돈이 걸린 업무라, 사용자 행위를 Audit·로깅으로 남기고 권한 기반 "
                       "접근으로 통제했습니다. 엑셀로는 불가능하던 변경 이력 추적을 기본값으로 "
                       "만들었습니다.",
                       "Since orders and settlement involve money, I logged user actions as an audit "
                       "trail and controlled access by role. Change-history tracking that was "
                       "impossible in spreadsheets became the default.")},
        ],
        "build": [
            {"module": L("고객 · 기관 · PI 관리", "Customer · institution · PI management"),
             "points": [
                 L("연구기관(기관 및 소속)·PI·고객 정보를 등록·조회·수정하는 거래처 마스터 관리 구현",
                   "Built client-master management to register, look up, and edit research "
                   "institutions (and affiliations), PIs, and customers"),
                 L("기관–PI–고객 소속 관계를 연계해 주문·정산의 기준 데이터로 활용",
                   "Linked institution–PI–customer affiliations and used them as the reference data "
                   "for orders and settlement"),
             ]},
            {"module": L("견적 · 주문 · 샘플", "Quote · order · sample"),
             "points": [
                 L("견적서 등록·조회·인쇄와 주문 등록(기본정보·샘플정보·주문회계)을 연계한 주문 프로세스 구현",
                   "Built an order process linking quote registration/lookup/printing with order "
                   "entry (basic info, sample info, order accounting)"),
                 L("유전체 검사 샘플의 수집일자·반환 여부 등 상태를 주문 단위로 관리",
                   "Managed genomics-test sample status — collection date, return status — per order"),
             ]},
            {"module": L("PI 선불계정 정산 · 회계", "PI prepaid-account settlement · accounting"),
             "points": [
                 L("회계기관계정에서 PI 선불계정으로 금액 이동(충전), PI 계정 간 이체는 별도 경로로 처리하고 잔액 초과를 검증",
                   "Handled fund moves (top-ups) from the accounting-institution account to PI "
                   "prepaid accounts, processed PI-to-PI transfers on a separate path, and validated "
                   "against over-balance"),
                 L("주문 시 주문총액과 PI 잔액 비교(잔액 부족 시 경고), 잔액·미수금 관리",
                   "Compared order total against PI balance at order time (warning on shortfall) and "
                   "managed balance and receivables"),
                 L("결제·입금 등록/취소/환불 연동, 취소·환불 시 회계기관계정 결제누적·입금총액 재정합",
                   "Linked payment/deposit registration, cancellation, and refund, reconciling the "
                   "accounting-institution account's cumulative payment and deposit totals on cancel/refund"),
             ]},
            {"module": L("공통 기반", "Common foundation"),
             "points": [
                 L("사용자 행위 Audit·로깅 이력 관리", "Audit logging and history of user actions"),
                 L("권한 기반 접근 제어", "Role-based access control"),
                 L("페이징·검색 표준 화면", "Standard paging and search screens"),
             ]},
        ],
        "result": {
            "metrics": [
                {"value": L("엑셀 → 단일 시스템", "Excel → one system"),
                 "label": L("흩어진 주문·정산 업무 일원화", "Consolidated scattered order/settlement work")},
                {"value": L("전 변경 감사 추적", "Full audit trail"),
                 "label": L("주문·정산 변경 이력 기록·추적", "Order/settlement change history recorded")},
            ],
            "retro": L("선불계정 잔액 검증과 감사 추적을 시스템의 기본값으로 만든 덕에, 엑셀로 "
                       "주고받던 주문·정산이 한 화면에서 맞춰지고 변경 이력까지 남게 됐습니다.",
                       "Because prepaid-balance validation and the audit trail became system "
                       "defaults, orders and settlement once exchanged in spreadsheets now reconcile "
                       "on one screen, with change history retained."),
        },
    },
    {
        "id": "cs5", "slug": "ib", "code": "CS5", "accent": "purple",
        "name": L("B2C 개인 맞춤 영양제 추천 (IB)", "B2C Personalized Supplement Recommendation (IB)"),
        "period": "2022.08 ~ 2023.07",
        "card_one_liner": L("설문·건강검진 결합 추천 + KCP 결제 + 리포트 자동화",
                            "Survey + health-checkup recommendation + KCP payment + report automation"),
        "card_stack": ["PHP", "MySQL", "KCP", "ClipSoft"],
        "hero": {
            "kicker": "CASE STUDY · CS5 · 2022.08–2023.07",
            "title": L("유전자에서 추천으로, 다시 리포트로",
                       "From genes to recommendation, and back to a report"),
            "sub": L("제노코어비에스 AI분석개발팀 · B2C 맞춤 영양제 추천·보험 상담 연계",
                     "Genocore BS AI Analytics & Development Team · B2C personalized supplements & "
                     "insurance-consultation linkage"),
        },
        "figures": [
            {"cap": L("FIG.A — 추천 · 결제 · 리포트 데이터 플로우",
                      "FIG.A — Recommendation · payment · report data flow"),
             "file": "ib_flow.svg", "file_en": "ib_flow.en.svg"},
        ],
        "glance": {
            "role": L("플랫폼 API 연동·백오피스·결제 구축 담당 · 추천·리포트 자동화 연계",
                      "Responsible for platform API integration, back office, and payments · linked "
                      "recommendation and report automation"),
            "period": "2022.08 – 2023.07",
            "stack": ["PHP", "JavaScript", "MySQL", "Apache", L("KCP 결제", "KCP payment"), "ClipSoft",
                      "Open API", L("알림톡", "AlimTalk"), "Docker"],
            "key_result": L("설문·건강검진 결합 영양제 추천부터 결제·리포트 자동화까지 구축",
                            "Built the whole flow — survey + health-checkup recommendation through "
                            "payment and report automation"),
        },
        "problem": L(
            "고객 설문과 건강검진 결과(PHR)를 바탕으로 개인에게 맞는 영양제를 추천하는 B2C 서비스를 "
            "처음부터 끝까지 구축하는 일이었습니다. 추천이 설득력을 가지려면 상품 접수 단계의 설문 "
            "답변과 건강검진 결과를 결합해야 했고, 건강검진·신체나이 분석·유전자 검사 결과는 외부 "
            "API로 모아야 했습니다. 추천할 영양제 상품 목록은 협력사에서 받아 관리하고, 모은 건강 "
            "데이터는 고객 동의 범위 안에서 보험 상담으로 연결해야 했습니다. 결제가 안전하게 끝나고 "
            "결과가 고객이 읽을 수 있는 건강 리포트로 자동 정리되는 것까지가 과제였습니다.",
            "This was building a B2C service end to end that recommends supplements suited to each "
            "person based on customer surveys and health-checkup results (PHR). For the "
            "recommendation to be convincing, it had to combine survey answers from the intake "
            "stage with health-checkup results, and the checkup, body-age analysis, and genetic-"
            "test results had to be gathered via external APIs. The supplement product list was "
            "received from a partner and managed, and the collected health data had to be linked to "
            "insurance consultation within the customer's consent. The scope reached all the way to "
            "completing payment securely and compiling the results automatically into a health "
            "report the customer can read.",
        ),
        "decisions": [
            {"head": L("추천은 설문과 건강검진 결과를 결합해 만든다",
                       "Build the recommendation by combining survey and checkup results"),
             "body": L("상품 접수 단계에서 받은 고객 설문 답변과 건강검진 결과(PHR)를 함께 반영해, "
                       "개인별 영양제를 추천하는 알고리즘을 구성했습니다.",
                       "Composed an algorithm that recommends supplements per person, drawing on "
                       "both the customer survey answers from the intake stage and the health-"
                       "checkup results (PHR).")},
            {"head": L("흩어진 건강 데이터는 외부 API로 모은다",
                       "Gather scattered health data via external APIs"),
             "body": L("건강검진 결과, 협력사의 신체나이 분석, 질병 위험도를 예측하는 유전자 검사 결과를 "
                       "Open API·협력사 API로 실시간 연동했습니다. 영양제 상품 목록은 협력사에서 받아 "
                       "DB로 관리했습니다.",
                       "Integrated health-checkup results, a partner's body-age analysis, and "
                       "genetic-test results predicting disease risk in real time via Open APIs and "
                       "partner APIs. The supplement product list was received from the partner and "
                       "managed in the DB.")},
            {"head": L("민감 정보는 동의 범위 안에서만 다룬다",
                       "Handle sensitive data only within consent"),
             "body": L("건강검진·유전 정보 같은 민감 데이터를 고객이 동의한 범위에서만 수집·전달하도록 "
                       "접근 통제와 처리 경로를 설계했습니다. 보험도 직접 추천하지 않고, 동의받은 결과만 "
                       "상담자에게 전달하는 연계로 풀었습니다.",
                       "Designed access control and processing paths so sensitive data such as "
                       "checkup and genetic information is collected and shared only within customer "
                       "consent. Rather than recommending insurance directly, I solved it as a "
                       "linkage that passes only consented results to a consultant.")},
            {"head": L("리포트 양식 변경을 운영에서 흡수한다",
                       "Absorb report-form changes in operations"),
             "body": L("ClipSoft 기반 리포트에서 양식을 코드 배포 없이 바꿀 수 있도록 템플릿과 데이터 "
                       "매핑 계층을 분리했습니다. 잦은 양식 변경이 개발 일정에 묶이지 않게 했습니다.",
                       "Separated the template and data-mapping layers in the ClipSoft-based reports "
                       "so forms can change without a code deploy — keeping frequent form changes off "
                       "the development schedule.")},
        ],
        "build": [
            {"module": L("개인화 추천 · 데이터 연동", "Personalized recommendation · data integration"),
             "points": [
                 L("건강검진 결과(PHR)·신체나이 분석·유전자 검사 결과를 Open API·협력사 API로 실시간 수집",
                   "Collected health-checkup results (PHR), body-age analysis, and genetic-test "
                   "results in real time via Open APIs and partner APIs"),
                 L("상품 접수 단계의 고객 설문 답변과 건강검진 결과를 결합한 개인화 영양제 추천 알고리즘 구현",
                   "Implemented a personalized supplement-recommendation algorithm combining intake "
                   "survey answers with health-checkup results"),
                 L("협력사에서 전달받은 영양제 상품 목록을 DB에 적재·관리해 추천 결과에 맞춰 노출",
                   "Loaded and managed the partner's supplement product list in the DB and surfaced "
                   "it to match recommendations"),
                 L("보험은 직접 추천 대신, 동의받은 건강검진·신체나이·유전자 결과를 보험 상담자에게 제공하는 상담 연계로 설계",
                   "Designed insurance not as a direct recommendation but as a consultation linkage "
                   "providing consented checkup, body-age, and genetic results to a consultant"),
             ]},
            {"module": L("결제 시스템", "Payment system"),
             "points": [
                 L("KCP 결제 모듈 연동으로 주문–결제 프로세스 구축",
                   "Built the order-payment process by integrating the KCP payment module"),
                 L("결제 예외·검증 처리로 결제 안정성 확보",
                   "Secured payment stability with payment-exception and validation handling"),
             ]},
            {"module": L("건강 리포트 자동화", "Health-report automation"),
             "points": [
                 L("ClipSoft 기반 개인 맞춤 건강 리포트 자동 생성",
                   "Auto-generated personalized health reports with ClipSoft"),
                 L("양식 변경을 코드 배포 없이 반영하도록 템플릿·데이터 매핑 계층 분리",
                   "Separated template and data-mapping layers so form changes apply without a code deploy"),
                 L("알림톡 연계로 리포트 발송·고객 커뮤니케이션 자동화",
                   "Automated report delivery and customer communication via AlimTalk"),
             ]},
            {"module": L("관리자 백오피스", "Admin back office"),
             "points": [
                 L("고객 관리·주문 관리·데이터 분석 인터페이스를 갖춘 통합 운영 백오피스 구축",
                   "Built an integrated operations back office with customer management, order "
                   "management, and data-analysis interfaces"),
             ]},
        ],
        "result": {
            "metrics": [
                {"value": L("추천→결제→리포트", "Recommend→pay→report"),
                 "label": L("한 흐름으로 자동화한 B2C 서비스", "A B2C service automated as one flow")},
                {"value": L("양식 무배포 변경", "No-deploy form changes"),
                 "label": L("ClipSoft 템플릿·데이터 매핑 분리", "ClipSoft template/data-mapping split")},
            ],
            "retro": L("추천부터 결제·리포트까지 한 흐름으로 이어 두고 양식 변경을 운영에서 흡수하게 "
                       "만든 덕에, 자주 바뀌는 상품과 양식에도 서비스가 흔들리지 않았습니다.",
                       "Because I connected recommendation through payment and report as one flow and "
                       "let form changes be absorbed in operations, the service held steady even as "
                       "products and forms changed often."),
        },
    },
]
