import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.graphics.shapes import Drawing, Circle, String, Rect, Line, Polygon

DARK_GRAY = colors.HexColor("#333333")
MED_GRAY = colors.HexColor("#555555")
LIGHT_BORDER = colors.HexColor("#D0D0D0")
PINK_RED = colors.HexColor("#E53935")
PINK_BORDER = colors.HexColor("#FFCDD2")
PINK_BG = colors.HexColor("#FFF5F5")
GREEN_COLOR = colors.HexColor("#00C853")
GOLD_COLOR = colors.HexColor("#F59E0B")

def create_header_drawing():
    d = Drawing(515, 45)
    # Logo Icon
    d.add(Circle(14, 32, 9, strokeColor=GOLD_COLOR, strokeWidth=2.5, fillColor=colors.HexColor("#FFFBEB")))
    d.add(Line(20, 26, 26, 20, strokeColor=GOLD_COLOR, strokeWidth=2.5))
    d.add(Circle(14, 32, 4, strokeColor=colors.HexColor("#3B82F6"), strokeWidth=1.5, fillColor=None))

    # Text: Plagiarism Detector
    d.add(String(32, 28, "Plagiarism", fontName="Helvetica-Bold", fontSize=13, fillColor=colors.HexColor("#111827")))
    d.add(String(100, 28, "Detector", fontName="Helvetica", fontSize=13, fillColor=colors.HexColor("#111827")))

    # Badge: .net
    d.add(Rect(154, 27, 24, 12, rx=2, ry=2, fillColor=colors.HexColor("#FBBF24"), strokeColor=None))
    d.add(String(156, 29, ".net", fontName="Helvetica-Bold", fontSize=7.5, fillColor=colors.black))

    # Report Page Subtitle
    d.add(String(0, 6, "Plagiarism Detector Report Page", fontName="Helvetica-Bold", fontSize=14, fillColor=DARK_GRAY))
    return d

def create_card1_drawing():
    d = Drawing(167, 115)
    # Outer box
    d.add(Rect(0, 0, 167, 115, rx=7, ry=7, strokeColor=LIGHT_BORDER, strokeWidth=1, fillColor=colors.white))
    # Title
    d.add(String(83.5, 99, "Plagiarism Score", fontName="Helvetica", fontSize=9, textAnchor="middle", fillColor=DARK_GRAY))
    
    # Donut Chart Left
    cx, cy, r = 44, 56, 26
    d.add(Circle(cx, cy, r, strokeColor=colors.HexColor("#ECEFF1"), strokeWidth=6, fillColor=None))
    d.add(Circle(cx, cy, r, strokeColor=PINK_RED, strokeWidth=6, fillColor=None)) # Small 6% arc simulated
    # Center White Mask to make donut
    d.add(Circle(cx, cy, r - 3, strokeColor=None, fillColor=colors.white))
    d.add(String(cx, cy - 5, "6%", fontName="Helvetica-Bold", fontSize=13, textAnchor="middle", fillColor=PINK_RED))

    # Right side match boxes
    # Box 1: 6% Exact Match
    d.add(Rect(88, 62, 70, 17, rx=3, ry=3, strokeColor=PINK_BORDER, strokeWidth=1, fillColor=PINK_BG))
    d.add(String(92, 67, "6%", fontName="Helvetica-Bold", fontSize=7.5, fillColor=PINK_RED))
    d.add(String(106, 67, "Exact Match", fontName="Helvetica", fontSize=7, fillColor=MED_GRAY))

    # Box 2: 0% Partial Match
    d.add(Rect(88, 41, 70, 17, rx=3, ry=3, strokeColor=colors.HexColor("#E0E0E0"), strokeWidth=1, fillColor=colors.white))
    d.add(String(92, 46, "0%", fontName="Helvetica-Bold", fontSize=7.5, fillColor=colors.HexColor("#9E9E9E")))
    d.add(String(106, 46, "Partial Match", fontName="Helvetica", fontSize=7, fillColor=MED_GRAY))

    # Bottom Badge: Fully Original / Partially Original
    d.add(Rect(14, 11, 60, 15, rx=3, ry=3, strokeColor=colors.HexColor("#FFCDD2"), strokeWidth=1, fillColor=colors.HexColor("#FFEBEE")))
    d.add(String(44, 15.5, "Partially Original", fontName="Helvetica-Bold", fontSize=6.2, textAnchor="middle", fillColor=PINK_RED))
    return d

def create_card2_drawing():
    d = Drawing(167, 115)
    d.add(Rect(0, 0, 167, 115, rx=7, ry=7, strokeColor=LIGHT_BORDER, strokeWidth=1, fillColor=colors.white))
    d.add(String(83.5, 99, "Unique Score", fontName="Helvetica", fontSize=9, textAnchor="middle", fillColor=DARK_GRAY))
    
    # Donut Chart Center
    cx, cy, r = 83.5, 52, 28
    d.add(Circle(cx, cy, r, strokeColor=GREEN_COLOR, strokeWidth=6.5, fillColor=None))
    d.add(Circle(cx, cy, r - 3.5, strokeColor=None, fillColor=colors.white))
    d.add(String(cx, cy - 6, "94%", fontName="Helvetica-Bold", fontSize=16, textAnchor="middle", fillColor=GREEN_COLOR))
    return d

def create_card3_drawing():
    d = Drawing(167, 115)
    d.add(Rect(0, 0, 167, 115, rx=7, ry=7, strokeColor=LIGHT_BORDER, strokeWidth=1, fillColor=colors.white))
    d.add(String(83.5, 99, "AI Detection Score", fontName="Helvetica", fontSize=9, textAnchor="middle", fillColor=DARK_GRAY))
    
    # Donut Chart Center with ?
    cx, cy, r = 83.5, 60, 26
    d.add(Circle(cx, cy, r, strokeColor=colors.HexColor("#CFD8DC"), strokeWidth=4, fillColor=None))
    d.add(String(cx, cy - 7, "?", fontName="Helvetica-Bold", fontSize=21, textAnchor="middle", fillColor=colors.HexColor("#78909C")))

    # AI text bottom
    d.add(String(83.5, 22, "AI detection not performed. Scan with", fontName="Helvetica", fontSize=6.2, textAnchor="middle", fillColor=colors.HexColor("#757575")))
    d.add(String(83.5, 12, "Plagiarism Detector to view results.", fontName="Helvetica-Bold", fontSize=6.2, textAnchor="middle", fillColor=colors.HexColor("#7E57C2")))
    return d

def create_stats_bar():
    d = Drawing(515, 34)
    # Outer Pill Border
    d.add(Rect(0, 0, 515, 34, rx=17, ry=17, strokeColor=colors.HexColor("#9E9E9E"), strokeWidth=1.2, fillColor=colors.white))
    
    # Dividers
    d.add(Line(128, 0, 128, 34, strokeColor=colors.HexColor("#E0E0E0"), strokeWidth=1))
    d.add(Line(257, 0, 257, 34, strokeColor=colors.HexColor("#E0E0E0"), strokeWidth=1))
    d.add(Line(386, 0, 386, 34, strokeColor=colors.HexColor("#E0E0E0"), strokeWidth=1))

    # Segment 1
    d.add(String(20, 13, "Total Words", fontName="Helvetica", fontSize=8, fillColor=DARK_GRAY))
    d.add(String(95, 13, "986", fontName="Helvetica", fontSize=8.5, fillColor=colors.black))

    # Segment 2
    d.add(String(142, 13, "Total Characters", fontName="Helvetica", fontSize=8, fillColor=DARK_GRAY))
    d.add(String(225, 13, "7743", fontName="Helvetica", fontSize=8.5, fillColor=colors.black))

    # Segment 3
    d.add(String(272, 13, "Plagiarized Sentences", fontName="Helvetica", fontSize=8, fillColor=DARK_GRAY))
    d.add(String(365, 13, "63", fontName="Helvetica", fontSize=8.5, fillColor=colors.black))

    # Segment 4
    d.add(String(398, 13, "Unique Sentences", fontName="Helvetica", fontSize=8, fillColor=DARK_GRAY))
    d.add(String(480, 13, "100%", fontName="Helvetica", fontSize=8.5, fillColor=colors.black))
    return d

def create_decorative_divider():
    d = Drawing(515, 16)
    # Left Line with Circle Endpoint
    d.add(Circle(20, 8, 3, fillColor=GOLD_COLOR, strokeColor=None))
    d.add(Line(20, 8, 235, 8, strokeColor=GOLD_COLOR, strokeWidth=1.5))

    # Center Diamonds / Stars
    # Diamond 1
    d.add(Polygon([240, 8, 244, 12, 248, 8, 244, 4], fillColor=GOLD_COLOR, strokeColor=None))
    # Star / Diamond 2
    d.add(Polygon([253, 8, 257.5, 13, 262, 8, 257.5, 3], fillColor=GOLD_COLOR, strokeColor=None))
    # Diamond 3
    d.add(Polygon([267, 8, 271, 12, 275, 8, 271, 4], fillColor=GOLD_COLOR, strokeColor=None))

    # Right Line with Circle Endpoint
    d.add(Line(280, 8, 495, 8, strokeColor=GOLD_COLOR, strokeWidth=1.5))
    d.add(Circle(495, 8, 3, fillColor=GOLD_COLOR, strokeColor=None))
    return d

def build_exact_plagiarism_pdf(filename="3_Plagiarism_Detector_Report_Gautham_Krishna.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=40,
        rightMargin=40,
        topMargin=32,
        bottomMargin=28
    )

    styles = getSampleStyleSheet()

    style_sec_title = ParagraphStyle(
        'SecTitle',
        fontName='Helvetica',
        fontSize=9.5,
        leading=13,
        textColor=DARK_GRAY
    )
    style_doc_title = ParagraphStyle(
        'DocTitle',
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=colors.black
    )
    style_content = ParagraphStyle(
        'ExactContent',
        fontName='Helvetica',
        fontSize=7.2,
        leading=10.2,
        alignment=TA_JUSTIFY,
        textColor=colors.HexColor("#263238")
    )
    style_page_num = ParagraphStyle(
        'PageNum',
        fontName='Helvetica',
        fontSize=7.5,
        alignment=TA_RIGHT,
        textColor=colors.HexColor("#616161")
    )

    story = []

    # ================= PAGE 1 =================
    story.append(create_header_drawing())
    story.append(Spacer(1, 10))

    # 3 Metric Cards side by side
    t_cards = Table([[create_card1_drawing(), create_card2_drawing(), create_card3_drawing()]], colWidths=[171.6, 171.6, 171.6])
    t_cards.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(t_cards)
    story.append(Spacer(1, 14))

    # Summary Stats Bar
    story.append(create_stats_bar())
    story.append(Spacer(1, 16))

    # Section Labels: Plagiarism Sources & References
    story.append(Paragraph("Plagiarism Sources", style_sec_title))
    story.append(Spacer(1, 12))
    story.append(Paragraph("References", style_sec_title))
    story.append(Spacer(1, 14))

    # Section Label: Document Content
    story.append(Paragraph("Document Content", style_doc_title))
    story.append(Spacer(1, 4))

    # Exact Content text with inline matched phrases in pink/red
    text_p1 = (
        "3.3 Study of Proposed System The proposed system combines multi-agent conversational reasoning with automated vulnerability detection. Rather than "
        "relying only on single-agent models or isolated static checks, the model evaluates the semantic and logic integrity of smart contracts for vulnerable execution "
        "paths. The framework uses data collected through empirical security benchmarks in Code4rena and Ethereum mainnet. The study examines contract functions "
        "and state variable transitions <font color='#E53935'>Department of Computer Science and Design,FISAT 10Advanced Smart Contract Vulnerability Detection via "
        "LLM-Powered Multi-Agent Systems</font> characteristics such as reentrancy paths, call execution flow, state update ordering, and authorization barriers. "
        "These characteristics are used to assess whether individual functions of the contract satisfy the security specifications of robust decentralized finance. "
        "The collected vulnerability information is incorporated into the multi-agent consensus process. This enables the model to identify execution paths that are "
        "dangerous for the targeted contract category. The model first seeks the most direct exploit path that satisfies the vulnerability constraints. When a fully "
        "verifiable exploit cannot be identified, it provides an alternative audit finding with minimal severity flags. The paper also presents a prototype multi-agent "
        "framework to support the practical auditing of code. The application is intended to communicate vulnerability findings based on collaborative decision-making, "
        "making the model more practical for smart contract developers. The overall approach connects contract ingestion, multi-agent analysis, and report generation in "
        "a single framework. 3.4 Requirement Specification The proposed auditing framework involves contract data collection, semantic vulnerability assessment, agent "
        "communication network, consensus evaluation, and the presentation of audit recommendations. Therefore, suitable data, processing capabilities, and software components "
        "are required to support the workflow. The study depends on the availability of reliable contract AST information about the target protocol. The collected data must "
        "describe the relevant security characteristics and support the evaluation of contracts for different vulnerability categories. A suitable computational "
        "environment is also required to process the agent dialogues and calculate consensus scores. 3.4.1 Recommended System Requirements The following "
        "requirements describe the general resources needed to support an automated multi-agent auditing framework. They should not be interpreted as exact hardware "
        "specifications reported by the paper: • Processor: A modern multi-core processor capable of handling concurrent agent reasoning data and token calculations. • Memory: "
        "Sufficient RAM to store and process contract logic information and benchmark audit data. • Storage: Adequate storage for contract source records, vulnerability "
        "attributes, benchmark datasets, and token usage information. • Location and Network Data: Stable internet connection for accessing remote LLM model APIs and "
        "blockchain testnets. • Execution Environment: A workstation capable of running Python 3.12 and Solidity compilation tools for accessing the prototype application and "
        "viewing audit summaries. <font color='#E53935'>Department of Computer Science and Design,FISAT 11Advanced Smart Contract Vulnerability Detection via LLM-Powered "
        "Multi-Agent Systems</font> • Network Connectivity: Connectivity required by the application for accessing cloud LLM endpoints and associated web3 services. "
        "3.4.2 Software Requirements The framework requires software components capable of processing smart contract ASTs, representing the agent conversation network, "
        "calculating vulnerability scores, and presenting the final audit results: • Data Processing: Software for storing, organising, and processing the vulnerability "
        "audit information. • Agent Network Representation: A suitable representation of conversational nodes and message exchanges with associated prompt attributes. • "
        "Auditing Component: A multi-agent consensus mechanism capable of evaluating vulnerability candidates based on BoT scenario templates and identifying genuine "
        "exploits. • Vulnerability Assessment: Software logic for evaluating vulnerability characteristics such as state variable updates, external calls, unchecked transfers, "
        "and authorization checks. • Mobile/Web Application: An application interface for presenting vulnerability warnings to developers. 3.5 Functional Requirements "
        "The accessibility and security routing framework should satisfy the following functional requirements: 1. The system shall use contract source and AST data "
        "collected through verified code repositories. 2. The system shall represent smart contract functions and logic blocks in a form suitable for agent debate. 3. The "
        "system shall consider reentrancy guards and execution ordering when assessing vulnerability risks. 4. The system shall consider access control design, signature "
        "verification, and delegatecall operations as security-critical infrastructure characteristics. 5. The system shall support vulnerability evaluation for common "
        "vulnerabilities, complex logic errors, and newly emerged CVEs. 6. The system shall identify the highest-confidence vulnerability exploit path when a vulnerable "
        "condition is present. 7. The system shall identify an alternative finding with minimal severity flags when a severe exploit is absent. <font color='#E53935'>Department "
        "of Computer Science and Design,FISAT 12Advanced Smart Contract Vulnerability Detection via LLM-Powered Multi-Agent Systems</font> 8. The system shall provide "
        "actionable remediation recommendations between an identified bug and its patch. 9. The system shall support the presentation of audit"
    )
    story.append(Paragraph(text_p1, style_content))
    story.append(Spacer(1, 10))

    # Page 1 Number
    story.append(Paragraph("Page 1 of 2", style_page_num))
    story.append(PageBreak())

    # ================= PAGE 2 =================
    text_p2 = (
        "recommendations through the prototype multi-agent application. 3.6 Non-Functional Requirements The smart contract vulnerability detection framework should "
        "satisfy the following non-functional requirements: • Usability: Route recommendations and vulnerability warnings should be presented clearly so that smart contract "
        "developers can understand and use the information. • Accessibility: The navigation and reporting interface should consider the needs of users with different security "
        "and Solidity development expertise. • Performance: The system should calculate suitable audit findings and consensus scores within a practical time. • Reliability: "
        "Audit recommendations should be based on consistent processing of the available contract logic data. • Accuracy: Vulnerability assessments should reflect the actual "
        "security characteristics recorded during the audit benchmarks. • Adaptability: The framework should accommodate different vulnerability categories and Solidity "
        "compiler versions for the supported categories of contracts. • Maintainability: Contract vulnerability records and prompt templates should be organised so that "
        "updates can be incorporated into the auditing process. • Safety and Inclusiveness: The system should support safer and more trustworthy smart contract deployment "
        "without assuming that a recommended contract is completely bug-free when complex logic anomalies remain. 3.7 Summary This chapter analysed the proof of concept, "
        "existing system, proposed system, and requirements of the multi-agent vulnerability detection framework for smart contract developers. The reviewed framework "
        "addresses the limitations of conventional static analysis by considering deep semantic code characteristics and the diverse requirements of decentralized application "
        "auditors. The proposed approach connects smart contract AST parsing with multi-agent collaborative debate and automated report generation. Its effectiveness "
        "depends on the quality and completeness of the available thought templates and LLM context depth. Overall, the framework provides an approach to improving smart "
        "contract security by incorporating multi-agent collaborative reasoning into decentralized software development. Department of Computer Science and Design,FISAT"
    )
    story.append(Paragraph(text_p2, style_content))
    story.append(Spacer(1, 25))

    # Decorative Gold Divider Line
    story.append(create_decorative_divider())
    story.append(Spacer(1, 35))

    # Page 2 Number
    story.append(Paragraph("Page 2 of 2", style_page_num))

    doc.build(story)
    print(f"Built exact plagiarism report: {filename}")

if __name__ == "__main__":
    build_exact_plagiarism_pdf()

