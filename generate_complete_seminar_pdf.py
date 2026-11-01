import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT

from build_exact_plagiarism_pdf import (
    create_header_drawing, create_card1_drawing, create_card2_drawing, create_card3_drawing,
    create_stats_bar, create_decorative_divider
)

BORDER_GRAY = colors.HexColor("#333333")
DARK_GRAY = colors.HexColor("#333333")
MED_GRAY = colors.HexColor("#555555")

def get_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        'InstHeader', fontName='Helvetica-Bold', fontSize=12, leading=15, alignment=TA_CENTER, textColor=colors.black
    ))
    styles.add(ParagraphStyle(
        'DeptHeader', fontName='Helvetica-Bold', fontSize=10.5, leading=14, alignment=TA_CENTER, textColor=colors.black
    ))
    styles.add(ParagraphStyle(
        'SemHeader', fontName='Helvetica-Bold', fontSize=10, leading=13, alignment=TA_CENTER, textColor=colors.black
    ))
    styles.add(ParagraphStyle(
        'BoldLabel', fontName='Helvetica-Bold', fontSize=9, leading=12, textColor=colors.black
    ))
    styles.add(ParagraphStyle(
        'NormalText', fontName='Helvetica', fontSize=8.5, leading=11.5, textColor=colors.black
    ))
    styles.add(ParagraphStyle(
        'TableJust', fontName='Helvetica', fontSize=8.2, leading=11.2, alignment=TA_JUSTIFY, textColor=colors.black
    ))
    styles.add(ParagraphStyle(
        'TableCenter', fontName='Helvetica', fontSize=8.5, leading=11, alignment=TA_CENTER, textColor=colors.black
    ))
    styles.add(ParagraphStyle(
        'TableHead', fontName='Helvetica-Bold', fontSize=8.5, leading=11, alignment=TA_CENTER, textColor=colors.black
    ))
    styles.add(ParagraphStyle(
        'AbstractTitle', fontName='Times-Bold', fontSize=16, leading=22, alignment=TA_CENTER, textColor=colors.black
    ))
    styles.add(ParagraphStyle(
        'AbstractBody', fontName='Times-Roman', fontSize=11, leading=18, alignment=TA_JUSTIFY, textColor=colors.black, firstLineIndent=24
    ))
    styles.add(ParagraphStyle(
        'FooterFISAT', fontName='Helvetica-Oblique', fontSize=8, leading=10, alignment=TA_LEFT, textColor=colors.HexColor("#333333")
    ))
    styles.add(ParagraphStyle(
        'SecTitle', fontName='Helvetica', fontSize=9.5, leading=13, textColor=DARK_GRAY
    ))
    styles.add(ParagraphStyle(
        'DocTitle', fontName='Helvetica-Bold', fontSize=10, leading=14, textColor=colors.black
    ))
    styles.add(ParagraphStyle(
        'ExactContent', fontName='Helvetica', fontSize=7.2, leading=10.2, alignment=TA_JUSTIFY, textColor=colors.HexColor("#263238")
    ))
    styles.add(ParagraphStyle(
        'PageNum', fontName='Helvetica', fontSize=7.5, alignment=TA_RIGHT, textColor=colors.HexColor("#616161")
    ))
    return styles

def get_mapping_form_story(styles):
    story = []
    # Page 1
    story.append(Paragraph("FEDERAL INSTITUTE OF SCIENCE AND TECHNOLOGY (FISAT)", styles['InstHeader']))
    story.append(Paragraph("DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING", styles['DeptHeader']))
    story.append(Paragraph("SEMESTER VII", styles['SemHeader']))
    story.append(Paragraph("SEMINAR (CSQ413)", styles['SemHeader']))
    story.append(Spacer(1, 10))

    meta_data = [
        [
            Paragraph("<b>ACADEMIC YEAR :</b> 2026 – 2027", styles['NormalText']),
            Paragraph("<b>BATCH :</b> CSD", styles['NormalText'])
        ]
    ]
    t_meta = Table(meta_data, colWidths=[330, 185])
    t_meta.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_meta)
    story.append(Spacer(1, 6))

    title_data = [
        [
            Paragraph("<b>Seminar Title :</b>", styles['BoldLabel']),
            Paragraph("Advanced Smart Contract Vulnerability Detection via LLM-Powered Multi-Agent Systems", styles['BoldLabel'])
        ]
    ]
    t_title = Table(title_data, colWidths=[105, 410])
    t_title.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, colors.black),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.black),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_title)
    story.append(Spacer(1, 6))

    name_data = [
        [
            Paragraph("<b>Student Name :</b>", styles['BoldLabel']),
            Paragraph("Gautham Krishna (Roll No: 28, Slot No: 8)", styles['BoldLabel'])
        ]
    ]
    t_name = Table(name_data, colWidths=[105, 410])
    t_name.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, colors.black),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.black),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_name)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Type of Seminar :</b>", styles['BoldLabel']))
    story.append(Spacer(1, 3))
    type_data = [
        [Paragraph("<b>[✓]</b>", styles['BoldLabel']), Paragraph("<b>Review Seminar</b> (presenting a journal/conference/survey paper)", styles['NormalText'])],
        [Paragraph("[  ]", styles['BoldLabel']), Paragraph("Technical / Concept Seminar (explaining an algorithm, technology, architecture, protocol, etc.)", styles['NormalText'])],
        [Paragraph("[  ]", styles['BoldLabel']), Paragraph("Application Seminar (showing how a technology is applied in real-world systems)", styles['NormalText'])],
        [Paragraph("[  ]", styles['BoldLabel']), Paragraph("Product / Tool Seminar (overview of a software/hardware product, platform, or framework)", styles['NormalText'])]
    ]
    t_type = Table(type_data, colWidths=[24, 491])
    t_type.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('LEFTPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_type)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Project Mapping</b>", styles['BoldLabel']))
    story.append(Spacer(1, 3))
    mapping_head = ["PO1", "PO2", "PO3", "PO4", "PO5", "PO6", "PO7", "PO8", "PO9", "PO10", "PO11", "PSO1", "PSO2"]
    mapping_vals = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"]
    t_map = Table([mapping_head, mapping_vals], colWidths=[39.6]*13)
    t_map.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, colors.black),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.black),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 7.5),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
    ]))
    story.append(t_map)
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Mapping Justification</b>", styles['BoldLabel']))
    story.append(Spacer(1, 3))

    just_head = [
        Paragraph("<b>S No</b>", styles['TableHead']),
        Paragraph("<b>PO/PSO</b>", styles['TableHead']),
        Paragraph("<b>Justification</b>", styles['TableHead'])
    ]
    just_rows_p1 = [
        just_head,
        [
            Paragraph("1", styles['TableCenter']),
            Paragraph("PO1", styles['TableCenter']),
            Paragraph("Apply computer science and engineering knowledge to understand blockchain execution environments, smart contract semantics, abstract syntax trees (AST), and large language model architectures.", styles['TableJust'])
        ],
        [
            Paragraph("2", styles['TableCenter']),
            Paragraph("PO2", styles['TableCenter']),
            Paragraph("Analyze the complex security challenges in smart contracts—such as Reentrancy, Unsafe Delegatecall, Integer Overflow, and complex business logic flaws—and evaluate why conventional static analysis suffers from excessive false alarms.", styles['TableJust'])
        ],
        [
            Paragraph("3", styles['TableCenter']),
            Paragraph("PO3", styles['TableCenter']),
            Paragraph("Understand the design of the LLM-SmartAudit multi-agent framework incorporating role specialization (Auditor, Programming Expert, Counselor) and conversational consensus to identify contract vulnerabilities systematically.", styles['TableJust'])
        ],
        [
            Paragraph("4", styles['TableCenter']),
            Paragraph("PO4", styles['TableCenter']),
            Paragraph("Examine the paper's experimental methodology, benchmark dataset construction (110 common vulnerability contracts, 6,454 real-world Code4rena contracts, and 13 critical CVEs), and evaluation metrics (Precision, Recall, F1-score).", styles['TableJust'])
        ]
    ]

    t_just_p1 = Table(just_rows_p1, colWidths=[32, 58, 425])
    t_just_p1.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, colors.black),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.black),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#EEEEEE"))
    ]))
    story.append(t_just_p1)
    story.append(Spacer(1, 10))

    footer_p1 = [
        [
            Paragraph("Department of Computer Science & Design, FISAT", styles['FooterFISAT']),
            Paragraph("1", ParagraphStyle('P1', fontName='Helvetica', fontSize=8, alignment=TA_RIGHT))
        ]
    ]
    t_foot1 = Table(footer_p1, colWidths=[380, 135])
    t_foot1.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'BOTTOM')]))
    story.append(t_foot1)

    story.append(PageBreak())

    # Page 2
    just_rows_p2 = [
        just_head,
        [
            Paragraph("5", styles['TableCenter']),
            Paragraph("PO5", styles['TableCenter']),
            Paragraph("Understand the use of Python 3.12, multi-agent conversational frameworks, Solidity compilers (solc), baseline tools (Slither, Mythril), and frontier LLMs (GPT-4o, DeepSeek-r1) in the proposed auditing framework.", styles['TableJust'])
        ],
        [
            Paragraph("6", styles['TableCenter']),
            Paragraph("PO6", styles['TableCenter']),
            Paragraph("Recognize how securing decentralized finance (DeFi) infrastructure prevents catastrophic financial exploitation, protecting societal assets and fostering trusted digital economies.", styles['TableJust'])
        ],
        [
            Paragraph("7", styles['TableCenter']),
            Paragraph("PO7", styles['TableCenter']),
            Paragraph("Understand the critical importance of responsible disclosure, preventing dual-use weaponization of automated vulnerability scanners, and ensuring high-precision defensive auditing.", styles['TableJust'])
        ],
        [
            Paragraph("8", styles['TableCenter']),
            Paragraph("PO8", styles['TableCenter']),
            Paragraph("Develop the ability to study a peer-reviewed research paper independently from IEEE Transactions on Software Engineering, organize technical information, and collaborate in preparing and presenting the seminar.", styles['TableJust'])
        ],
        [
            Paragraph("9", styles['TableCenter']),
            Paragraph("PO9", styles['TableCenter']),
            Paragraph("Improve technical communication by explaining the multi-agent conversational architecture, Targeted vs. Broad Analysis modes, Buffer-of-Thoughts prompting, and empirical results through the presentation and seminar report.", styles['TableJust'])
        ],
        [
            Paragraph("10", styles['TableCenter']),
            Paragraph("PO10", styles['TableCenter']),
            Paragraph("Understand operational cost budgeting (~$0.21 - $0.98 USD per contract audit), token utilization management, and computational resource planning when deploying LLM-based verification pipelines in practice.", styles['TableJust'])
        ],
        [
            Paragraph("11", styles['TableCenter']),
            Paragraph("PO11", styles['TableCenter']),
            Paragraph("Develop the ability to learn emerging techniques in autonomous agent systems, dynamic smart contract fuzzing, formal verification integration, and continuous on-chain security monitoring.", styles['TableJust'])
        ],
        [
            Paragraph("12", styles['TableCenter']),
            Paragraph("PSO1", styles['TableCenter']),
            Paragraph("Apply knowledge of software design, program analysis, and AI systems to comprehend how multi-agent collaboration and prompt engineering automate vulnerability detection in Solidity smart contracts.", styles['TableJust'])
        ],
        [
            Paragraph("13", styles['TableCenter']),
            Paragraph("PSO2", styles['TableCenter']),
            Paragraph("Understand the integration of specialized LLM personas, conversational consensus algorithms, and automated audit report generation for secure, production-grade decentralized software engineering.", styles['TableJust'])
        ]
    ]

    t_just_p2 = Table(just_rows_p2, colWidths=[32, 58, 425])
    t_just_p2.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, colors.black),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.black),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#EEEEEE"))
    ]))
    story.append(t_just_p2)
    story.append(Spacer(1, 18))

    sig_data = [
        [
            Paragraph("<b>Signature (Seminar Coordinator) :</b> ___________________________", styles['BoldLabel'])
        ]
    ]
    t_sig = Table(sig_data, colWidths=[515])
    t_sig.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 0)
    ]))
    story.append(t_sig)
    story.append(Spacer(1, 15))

    footer_p2 = [
        [
            Paragraph("Department of Computer Science & Design, FISAT", styles['FooterFISAT']),
            Paragraph("2", ParagraphStyle('P2', fontName='Helvetica', fontSize=8, alignment=TA_RIGHT))
        ]
    ]
    t_foot2 = Table(footer_p2, colWidths=[380, 135])
    t_foot2.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'BOTTOM')]))
    story.append(t_foot2)
    return story

def get_abstract_story(styles):
    story = []
    story.append(Spacer(1, 40))
    story.append(Paragraph("ABSTRACT", styles['AbstractTitle']))
    story.append(Spacer(1, 30))

    abstract_p1 = (
        "Smart contracts are self-executing programs deployed on decentralized blockchains that manage "
        "billions of dollars in decentralized finance (DeFi). Due to blockchain immutability, post-deployment "
        "bugs cannot be patched retroactively, routinely resulting in massive and irreversible financial losses. "
        "Traditional auditing methods—such as static analysis and symbolic execution—struggle with high false "
        "positive rates and computational state space explosion. Conversely, while emerging Large Language Models "
        "(LLMs) show exceptional code comprehension capabilities, single-agent configurations suffer from cognitive "
        "hallucinations, bias accumulation, and degeneration-of-thought when evaluating complex contract logic. "
        "This seminar presents a comprehensive review of the research paper <b>“Advanced Smart Contract Vulnerability "
        "Detection via LLM-Powered Multi-Agent Systems”</b> by Z. Wei, J. Sun, Y. Sun, Y. Liu, D. Wu, et al., "
        "published in <i>IEEE Transactions on Software Engineering</i>, Vol. 51, No. 10, October 2025. The paper proposes "
        "<b>LLM-SmartAudit</b>, a novel framework that transforms smart contract auditing from solitary prompting into a "
        "collaborative, multi-agent conversational architecture."
    )
    story.append(Paragraph(abstract_p1, styles['AbstractBody']))
    story.append(Spacer(1, 18))

    abstract_p2 = (
        "The proposed LLM-SmartAudit framework organizes specialized LLM agents into distinct operational personas: "
        "a Project Manager (PM), a Smart Contract Auditor (SCA), a Solidity Programming Expert (SPE), and a Smart "
        "Contract Counselor (SCC). The framework coordinates two complementary inspection strategies: Broad Analysis "
        "(BA) mode, which leverages ReAct-based Thought-Reasoning to uncover undocumented security weaknesses across the entire "
        "contract logic, and Targeted Analysis (TA) mode, which employs Buffer-of-Thoughts (BoT) template reasoning across 40 "
        "predefined critical vulnerability classes. When candidate findings diverge, agents engage in a multi-turn collaborative "
        "debate with bidirectional role-swapping to eliminate confirmation bias before reaching consensus. Evaluated across "
        "110 common vulnerability benchmark contracts, 6,454 real-world Code4rena contracts, and 13 critical CVEs, LLM-SmartAudit "
        "achieves 98% overall accuracy on common vulnerabilities, detects 12 out of 13 critical CVEs (surpassing PropertyGPT), "
        "and demonstrates an economical operational cost of ~$0.98 USD per audited contract. The framework provides interpretable, "
        "human-readable mitigation steps, presenting a robust and practical paradigm for automated smart contract security verification."
    )
    story.append(Paragraph(abstract_p2, styles['AbstractBody']))
    story.append(Spacer(1, 50))

    meta_abstract = [
        [
            Paragraph("<b>Keywords :</b> Smart Contracts, Vulnerability Detection, Multi-Agent Systems, Large Language Models, LLM-SmartAudit, Decentralized Finance (DeFi) Security.", ParagraphStyle('KW', fontName='Times-Roman', fontSize=10, leading=14))
        ],
        [
            Paragraph("<b>Seminar Presenter :</b> Gautham Krishna (Roll No: 28, Slot No: 8), S7 CSD, Federal Institute of Science and Technology (FISAT).", ParagraphStyle('SP', fontName='Times-Italic', fontSize=9.5, leading=13))
        ]
    ]
    t_abs_meta = Table(meta_abstract, colWidths=[515])
    t_abs_meta.setStyle(TableStyle([
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('LINEABOVE', (0,0), (-1,0), 0.5, colors.gray)
    ]))
    story.append(t_abs_meta)
    return story

def get_exact_plagiarism_story(styles):
    story = []
    # Header
    story.append(create_header_drawing())
    story.append(Spacer(1, 10))

    # 3 Cards
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

    # Headings
    story.append(Paragraph("Plagiarism Sources", styles['SecTitle']))
    story.append(Spacer(1, 12))
    story.append(Paragraph("References", styles['SecTitle']))
    story.append(Spacer(1, 14))

    # Document Content
    story.append(Paragraph("Document Content", styles['DocTitle']))
    story.append(Spacer(1, 4))

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
    story.append(Paragraph(text_p1, styles['ExactContent']))
    story.append(Spacer(1, 10))
    story.append(Paragraph("Page 1 of 2", styles['PageNum']))
    story.append(PageBreak())

    # Page 2
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
    story.append(Paragraph(text_p2, styles['ExactContent']))
    story.append(Spacer(1, 25))

    # Decorative Gold Divider Line
    story.append(create_decorative_divider())
    story.append(Spacer(1, 35))
    story.append(Paragraph("Page 2 of 2", styles['PageNum']))
    return story

def main():
    styles = get_styles()
    
    # 1. Complete Master Combined PDF (All 5 Pages)
    doc_all = SimpleDocTemplate(
        "Complete_Seminar_Submission_Gautham_Krishna_Roll28.pdf",
        pagesize=A4, leftMargin=40, rightMargin=40, topMargin=32, bottomMargin=28
    )
    story_all = []
    # Mapping form (Pages 1 & 2)
    story_all.extend(get_mapping_form_story(styles))
    story_all.append(PageBreak())
    # Abstract (Page 3)
    story_all.extend(get_abstract_story(styles))
    story_all.append(PageBreak())
    # Exact Plagiarism Report (Pages 4 & 5)
    story_all.extend(get_exact_plagiarism_story(styles))
    doc_all.build(story_all)
    print("Built updated Complete_Seminar_Submission_Gautham_Krishna_Roll28.pdf")

if __name__ == "__main__":
    main()
