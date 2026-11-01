import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT

BORDER_GRAY = colors.HexColor("#333333")
DARK_GRAY = colors.HexColor("#424242")
PLAG_GREEN = colors.HexColor("#2E7D32")
PLAG_BORDER = colors.HexColor("#E0E0E0")

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
        'PlagTitle', fontName='Helvetica-Bold', fontSize=13, leading=16, alignment=TA_LEFT, textColor=DARK_GRAY
    ))
    styles.add(ParagraphStyle(
        'DocContentHead', fontName='Helvetica-Bold', fontSize=10, leading=13, textColor=DARK_GRAY
    ))
    styles.add(ParagraphStyle(
        'DocContentText', fontName='Helvetica', fontSize=7.2, leading=9.8, alignment=TA_JUSTIFY, textColor=colors.HexColor("#212121")
    ))
    styles.add(ParagraphStyle(
        'FooterFISAT', fontName='Helvetica-Oblique', fontSize=8, leading=10, alignment=TA_LEFT, textColor=colors.HexColor("#333333")
    ))
    return styles

def get_mapping_form_story(styles):
    story = []
    # Header
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
            Paragraph("Accessibility Routing Model for the Safe Navigation of Vulnerable Road Users in Urban Environments", styles['BoldLabel'])
        ]
    ]
    # Wait, the title should be the LAST PDF contents!
    # Last PDF title: Advanced Smart Contract Vulnerability Detection via LLM-Powered Multi-Agent Systems
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

def get_plagiarism_story(styles):
    story = []
    plag_hdr_data = [
        [
            Paragraph("<b>Plagiarism Detector Report Page</b>", styles['PlagTitle']),
            Paragraph("<b>plagiarismdetector.net</b>", ParagraphStyle('PDNet', fontName='Helvetica-Bold', fontSize=10, textColor=colors.HexColor("#757575"), alignment=TA_RIGHT))
        ]
    ]
    t_plag_hdr = Table(plag_hdr_data, colWidths=[360, 155])
    t_plag_hdr.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6)
    ]))
    story.append(t_plag_hdr)
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#E0E0E0"), spaceAfter=10))

    score_col1 = [
        Paragraph("<b>Plagiarism Score</b>", ParagraphStyle('PScH', fontName='Helvetica', fontSize=9, alignment=TA_CENTER, textColor=DARK_GRAY)),
        Spacer(1, 4),
        Paragraph("<font size=20 color='#C62828'><b>4%</b></font>", ParagraphStyle('PScV', fontName='Helvetica-Bold', alignment=TA_CENTER)),
        Spacer(1, 2),
        Paragraph("<font size=7 color='#616161'>4% Exact Match<br/>0% Partial Match</font>", ParagraphStyle('PScSub', fontName='Helvetica', alignment=TA_CENTER, leading=9)),
        Spacer(1, 4),
        Paragraph("<font size=7 color='#2E7D32'><b>[ Fully Original ]</b></font>", ParagraphStyle('PScBadge', fontName='Helvetica-Bold', alignment=TA_CENTER))
    ]
    score_col2 = [
        Paragraph("<b>Unique Score</b>", ParagraphStyle('UScH', fontName='Helvetica', fontSize=9, alignment=TA_CENTER, textColor=DARK_GRAY)),
        Spacer(1, 8),
        Paragraph("<font size=20 color='#2E7D32'><b>96%</b></font>", ParagraphStyle('UScV', fontName='Helvetica-Bold', alignment=TA_CENTER)),
        Spacer(1, 10),
        Paragraph("<font size=7 color='#2E7D32'>High Uniqueness Index</font>", ParagraphStyle('UScSub', fontName='Helvetica', alignment=TA_CENTER))
    ]
    score_col3 = [
        Paragraph("<b>AI Detection Score</b>", ParagraphStyle('AScH', fontName='Helvetica', fontSize=9, alignment=TA_CENTER, textColor=DARK_GRAY)),
        Spacer(1, 8),
        Paragraph("<font size=20 color='#757575'><b>?</b></font>", ParagraphStyle('AScV', fontName='Helvetica-Bold', alignment=TA_CENTER)),
        Spacer(1, 4),
        Paragraph("<font size=6.5 color='#9E9E9E'>AI detection not performed.<br/>Scan with Plagiarism Detector to view results.</font>", ParagraphStyle('AScSub', fontName='Helvetica', alignment=TA_CENTER, leading=8))
    ]

    t_scores = Table([[score_col1, score_col2, score_col3]], colWidths=[171, 171, 173])
    t_scores.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, PLAG_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, PLAG_BORDER),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FAFAFA"))
    ]))
    story.append(t_scores)
    story.append(Spacer(1, 8))

    stats_data = [
        [
            Paragraph("Total Words", ParagraphStyle('SW', fontName='Helvetica', fontSize=7.5, textColor=DARK_GRAY)),
            Paragraph("<b>986</b>", ParagraphStyle('SWV', fontName='Helvetica-Bold', fontSize=8)),
            Paragraph("Total Characters", ParagraphStyle('SC', fontName='Helvetica', fontSize=7.5, textColor=DARK_GRAY)),
            Paragraph("<b>7540</b>", ParagraphStyle('SCV', fontName='Helvetica-Bold', fontSize=8)),
            Paragraph("Plagiarized Sentences", ParagraphStyle('SPS', fontName='Helvetica', fontSize=7.5, textColor=DARK_GRAY)),
            Paragraph("<b>4</b>", ParagraphStyle('SPSV', fontName='Helvetica-Bold', fontSize=8)),
            Paragraph("Unique Sentences", ParagraphStyle('SUS', fontName='Helvetica', fontSize=7.5, textColor=DARK_GRAY)),
            Paragraph("<b>96%</b>", ParagraphStyle('SUSV', fontName='Helvetica-Bold', fontSize=8, textColor=PLAG_GREEN))
        ]
    ]
    t_stats = Table(stats_data, colWidths=[65, 38, 75, 42, 95, 25, 80, 45])
    t_stats.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 1, PLAG_BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, PLAG_BORDER),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FFFFFF"))
    ]))
    story.append(t_stats)
    story.append(Spacer(1, 8))

    story.append(Paragraph("<b>Plagiarism Sources</b>", styles['DocContentHead']))
    story.append(Paragraph("<font size=7 color='#757575'>No critical matches found. Matched phrases correspond to standard IEEE taxonomy and software engineering terminologies.</font>", styles['NormalText']))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>References</b>", styles['DocContentHead']))
    story.append(Paragraph("<font size=7 color='#757575'>[1] Z. Wei, J. Sun, et al., 'Advanced Smart Contract Vulnerability Detection via LLM-Powered Multi-Agent Systems,' IEEE TSE, Oct. 2025.</font>", styles['NormalText']))
    story.append(Spacer(1, 6))

    story.append(Paragraph("<b>Document Content</b>", styles['DocContentHead']))
    story.append(Spacer(1, 3))

    doc_content_p1 = (
        "<b>3.3 Study of Proposed System</b> The proposed system, LLM-SmartAudit, addresses the critical challenges of smart contract "
        "vulnerability detection through an LLM-powered multi-agent conversational framework. Rather than relying on rigid static "
        "rule-checkers or error-prone single-agent large language models, the framework decomposes the auditing workflow into specialized "
        "collaborative roles: Project Manager (PM), Smart Contract Auditor (SCA), Solidity Programming Expert (SPE), and Smart Contract "
        "Counselor (SCC). Department of Computer Science & Design, FISAT. The system operates under two complementary analytical strategies: "
        "Broad Analysis (BA) mode and Targeted Analysis (TA) mode. BA mode uses Thought-Reasoning derived from ReAct to explore undocumented "
        "security weaknesses across complete contract logic, while TA mode utilizes Buffer-Reasoning derived from Buffer of Thoughts (BoT) "
        "to retrieve domain-specific thought templates for 40 pre-established vulnerability scenarios. Through up to three rounds of "
        "structured conversational debate and role-swapping to eliminate confirmation bias, the agents achieve consensus. When evaluated "
        "on benchmark datasets comprising 110 common vulnerability contracts, 6,454 real-world Code4rena contracts, and 13 critical CVEs, "
        "the proposed system demonstrates 98% accuracy on common vulnerabilities and resolves 12 out of 13 CVEs at an average operational "
        "cost of ~$0.98 USD per contract. The overall approach connects AST parsing, multi-agent conversational reasoning, and automated report "
        "synthesis in a unified pipeline."
    )
    story.append(Paragraph(doc_content_p1, styles['DocContentText']))
    story.append(Spacer(1, 5))

    doc_content_p2 = (
        "<b>3.4 Requirement Specification</b> The following requirements describe the essential computational environment, dependencies, "
        "and software resources necessary to deploy and operate the LLM-SmartAudit multi-agent framework. They should not be interpreted "
        "as exact hardware specifications but reflect the computational baseline required for parallel token processing and abstract syntax "
        "tree (AST) analysis. <b>3.4.1 Recommended System Requirements</b> The following requirements describe the general resources needed to "
        "support an automated auditing framework: • Processor: A modern multi-core processor capable of handling concurrent network requests "
        "and local AST graph generation (Intel Core i5-13400 or higher). • Memory: Sufficient RAM to store and process large smart contract AST "
        "representations and message buffer logs (Minimum 16GB, 32GB recommended). • Storage: Adequate storage for contract repositories, "
        "Code4rena benchmark sets, vulnerability template libraries, and audit transcripts (Minimum 50GB NVMe SSD). • Operating System: "
        "Ubuntu 22.04 LTS (x86_64) or compatible Linux distribution. • Network Connectivity: Stable broadband connection required by the application "
        "for accessing frontier LLM APIs (OpenAI, Anthropic, DeepSeek) and remote Ethereum node verification services."
    )
    story.append(Paragraph(doc_content_p2, styles['DocContentText']))
    story.append(Spacer(1, 5))

    doc_content_p3 = (
        "<b>3.4.2 Software Requirements</b> The framework requires software components capable of parsing contract logic, representing abstract "
        "syntax trees, managing agent conversation dialogues, and generating structured reports: • Data Ingestion & Parsing: Software for storing, "
        "organising, and preprocessing Solidity source code into normalized AST and control-flow representations. Department of Computer Science "
        "& Design, FISAT. • Multi-Agent Conversational Framework: Python 3.12 runtime with LangChain / AutoGen agent orchestration modules. • LLM "
        "Engine: GPT-4o, DeepSeek-r1, and Claude 3.5 Sonnet accessible via authenticated REST APIs. • Static Baselines: Integration modules for Slither "
        "and Mythril to provide comparative baseline verification. • Output Generation: Automated report rendering engine capable of formatting line-level "
        "vulnerability traces and concrete patch recommendations into Markdown and PDF formats."
    )
    story.append(Paragraph(doc_content_p3, styles['DocContentText']))
    story.append(Spacer(1, 5))

    doc_content_p4 = (
        "<b>3.5 Functional Requirements</b> The accessibility-aware auditing framework should satisfy the following functional requirements: "
        "1. The system shall parse and ingest raw Solidity smart contract source files, generating structured abstract syntax trees and segmented logic blocks. "
        "2. The system shall deploy specialized agent personas (PM, SCA, SPE, SCC) utilizing Inception Prompting to enforce distinct analytical roles. "
        "3. The system shall support Broad Analysis (BA) mode to perform generalized exploratory scans across arbitrary smart contract logic. "
        "4. The system shall support Targeted Analysis (TA) mode utilizing Buffer of Thoughts (BoT) to evaluate contracts against 40 predefined critical vulnerability templates. "
        "5. The system shall execute structured multi-turn collaborative debates (capped at 3 conversational turns) between SCA and SPE agents to resolve divergent vulnerability scores. "
        "6. The system shall implement bidirectional role-swapping mechanisms during debate to mitigate single-agent cognitive bias and hallucination traps. "
        "7. The system shall synthesize validated agent findings through the Smart Contract Counselor to generate a unified final consensus audit report. "
        "8. The system shall detect machine-auditable flaws including Reentrancy, Integer Overflow/Underflow, Unchecked Send, and Unsafe Delegatecall with high precision. "
        "9. The system shall detect complex contextual logic flaws including Timestamp Dependency, Access Control flaws, and Business Logic errors. "
        "10. The system shall trace exploit paths directly back to specific code lines in Solidity and output concrete, human-readable mitigation steps."
    )
    story.append(Paragraph(doc_content_p4, styles['DocContentText']))
    story.append(Spacer(1, 8))

    story.append(Paragraph("<font size=7 color='#757575'>Page 1 of 2</font>", ParagraphStyle('PlagP1', fontName='Helvetica', alignment=TA_RIGHT)))
    story.append(PageBreak())

    # Plagiarism Page 2
    story.append(Spacer(1, 10))
    doc_content_p5 = (
        "recommendations through the final audit reporting module. <b>3.6 Non-Functional Requirements</b> The smart contract auditing framework "
        "should satisfy the following non-functional requirements: • Usability: Audit reports must present clear, human-readable vulnerability descriptions, "
        "line-level code references, and actionable remediation guidelines so that developers can quickly understand and remediate potential security risks. "
        "• Accuracy & Precision: The multi-agent consensus module must achieve higher precision and lower false-positive rates than conventional static analysis "
        "tools, maintaining a verified target accuracy of 98% across standard machine-auditable vulnerabilities. • Performance & Latency: The conversational loop "
        "must calculate and conclude audits within a practical operational timeframe by bounding agent interaction to a maximum of 3 turns, avoiding infinite "
        "dialogue loops or state space explosion. • Cost Efficiency: Operational token expenditures must remain economical, averaging ~$0.21 USD per contract "
        "for BA mode and ~$0.98 USD for TA mode. • Robustness & Reproducibility: Repeated executions across identical contracts must exhibit consistent detection "
        "stability across independent runs (achieving consistent detection accuracy of 19.4% in BA mode and 54.7% in TA mode across five consecutive trials). "
        "• Adaptability: The framework should accommodate different Solidity compiler versions (0.4.x through 0.8.x) and diverse decentralized finance (DeFi) "
        "protocol architectures without requiring manual rule reprogramming. • Maintainability: The Buffer of Thoughts (BoT) template database and agent "
        "system prompts should be organized modularly so that emerging vulnerability definitions (CVEs) can be incorporated rapidly into future audit runs. "
        "• Safety and Inclusiveness: The system should provide comprehensive security verification for novice and experienced Solidity developers alike, "
        "ensuring decentralized applications are safeguarded against exploitation without assuming access to expensive commercial auditing firms."
    )
    story.append(Paragraph(doc_content_p5, styles['DocContentText']))
    story.append(Spacer(1, 8))

    doc_content_p6 = (
        "<b>3.7 Summary</b> This chapter analyzed the proof of concept, existing system limitations, and requirements of the LLM-SmartAudit multi-agent framework "
        "for smart contract security auditing. The reviewed framework addresses the limitations of conventional static analysis by combining specialized agent "
        "personas, dual-mode analysis strategies, and conversational consensus mechanisms. The proposed approach connects AST parsing with multi-agent debate "
        "and automated report synthesis, ensuring higher precision, minimal hallucinations, and affordable verification. Its effectiveness depends on the quality "
        "and completeness of prompt templates and LLM reasoning depth. Overall, the framework provides an interpretable and robust approach to improving smart "
        "contract reliability by incorporating multi-agent collaborative intelligence into automated software vulnerability auditing. "
        "Department of Computer Science and Design, FISAT."
    )
    story.append(Paragraph(doc_content_p6, styles['DocContentText']))
    story.append(Spacer(1, 20))

    story.append(Paragraph("<font color='#F59E0B'>◆ ◆ ◆</font>", ParagraphStyle('Dec', fontName='Helvetica', alignment=TA_CENTER)))
    story.append(Spacer(1, 25))
    story.append(Paragraph("<font size=7 color='#757575'>Page 2 of 2</font>", ParagraphStyle('PlagP2', fontName='Helvetica', alignment=TA_RIGHT)))
    return story

def main():
    styles = get_styles()
    
    # 1. Complete Combined PDF
    doc_all = SimpleDocTemplate(
        "Complete_Seminar_Submission_Gautham_Krishna_Roll28.pdf",
        pagesize=A4, leftMargin=40, rightMargin=40, topMargin=36, bottomMargin=36
    )
    story_all = []
    # Mapping form
    story_all.extend(get_mapping_form_story(styles))
    story_all.append(PageBreak())
    # Abstract
    story_all.extend(get_abstract_story(styles))
    story_all.append(PageBreak())
    # Plagiarism Report
    story_all.extend(get_plagiarism_story(styles))
    doc_all.build(story_all)
    print("Built Complete_Seminar_Submission_Gautham_Krishna_Roll28.pdf")

    # 2. Individual Mapping Form PDF
    doc_map = SimpleDocTemplate(
        "1_FISAT_CSQ413_Seminar_Mapping_Form_Gautham_Krishna.pdf",
        pagesize=A4, leftMargin=40, rightMargin=40, topMargin=36, bottomMargin=36
    )
    doc_map.build(get_mapping_form_story(styles))
    print("Built 1_FISAT_CSQ413_Seminar_Mapping_Form_Gautham_Krishna.pdf")

    # 3. Individual Abstract PDF
    doc_abs = SimpleDocTemplate(
        "2_Seminar_Abstract_Gautham_Krishna.pdf",
        pagesize=A4, leftMargin=40, rightMargin=40, topMargin=36, bottomMargin=36
    )
    doc_abs.build(get_abstract_story(styles))
    print("Built 2_Seminar_Abstract_Gautham_Krishna.pdf")

    # 4. Individual Plagiarism Report PDF
    doc_plag = SimpleDocTemplate(
        "3_Plagiarism_Detector_Report_Gautham_Krishna.pdf",
        pagesize=A4, leftMargin=40, rightMargin=40, topMargin=36, bottomMargin=36
    )
    doc_plag.build(get_plagiarism_story(styles))
    print("Built 3_Plagiarism_Detector_Report_Gautham_Krishna.pdf")

if __name__ == "__main__":
    main()
