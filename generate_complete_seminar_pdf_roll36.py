import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT

from build_exact_plagiarism_pdf_roll36 import (
    create_header_drawing, create_card1_drawing, create_card2_drawing, create_card3_drawing,
    create_stats_bar, create_decorative_divider
)

DARK_GRAY = colors.HexColor("#333333")

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
            Paragraph("Demystifying Defects: Federated Learning and Explainable AI for Semiconductor Fault Detection", styles['BoldLabel'])
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
            Paragraph("Joseph D Poonoly (Roll No: 36, Slot No: 27)", styles['BoldLabel'])
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
            Paragraph("Apply computer science and engineering knowledge to understand distributed machine learning, convolutional neural networks, federated averaging, and gradient optimization.", styles['TableJust'])
        ],
        [
            Paragraph("2", styles['TableCenter']),
            Paragraph("PO2", styles['TableCenter']),
            Paragraph("Analyze semiconductor wafer defect patterns (center, donut, edge-ring, mixed types) and examine the privacy limitations of centralized training across proprietary fabrication facilities.", styles['TableJust'])
        ],
        [
            Paragraph("3", styles['TableCenter']),
            Paragraph("PO3", styles['TableCenter']),
            Paragraph("Understand the design of a privacy-preserving federated inspection framework combining ResNet152 backbones, FedAvg aggregation, differential privacy, and explainable AI.", styles['TableJust'])
        ],
        [
            Paragraph("4", styles['TableCenter']),
            Paragraph("PO4", styles['TableCenter']),
            Paragraph("Examine the benchmark dataset (MixedWM38 with 38,000+ images), exploratory data analysis, PCA dimensionality reduction, and evaluation metrics across 10 communication rounds.", styles['TableJust'])
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
            Paragraph("Understand the use of PyTorch, differential privacy libraries, Grad-CAM, LIME, and t-SNE visualization tools in implementing the semiconductor fault detection framework.", styles['TableJust'])
        ],
        [
            Paragraph("6", styles['TableCenter']),
            Paragraph("PO6", styles['TableCenter']),
            Paragraph("Recognize how automated defect detection in semiconductor manufacturing enhances hardware quality, device reliability, and cost efficiency in automotive and medical electronics.", styles['TableJust'])
        ],
        [
            Paragraph("7", styles['TableCenter']),
            Paragraph("PO7", styles['TableCenter']),
            Paragraph("Understand the importance of data confidentiality in industrial AI, safeguarding proprietary wafer map designs through differential privacy without exposing IP.", styles['TableJust'])
        ],
        [
            Paragraph("8", styles['TableCenter']),
            Paragraph("PO8", styles['TableCenter']),
            Paragraph("Develop the ability to independently study peer-reviewed IEEE Access research, organize technical findings, and collaborate in preparing and presenting the seminar.", styles['TableJust'])
        ],
        [
            Paragraph("9", styles['TableCenter']),
            Paragraph("PO9", styles['TableCenter']),
            Paragraph("Improve technical communication by clearly explaining federated aggregation formulas, Gaussian noise injection, Grad-CAM heatmaps, and performance benchmarks.", styles['TableJust'])
        ],
        [
            Paragraph("10", styles['TableCenter']),
            Paragraph("PO10", styles['TableCenter']),
            Paragraph("Understand resource planning, communication round budgets, and computational requirements when deploying federated learning models across distributed manufacturing fabs.", styles['TableJust'])
        ],
        [
            Paragraph("11", styles['TableCenter']),
            Paragraph("PO11", styles['TableCenter']),
            Paragraph("Develop the ability to explore emerging frontiers in edge federated learning, MLOps CI/CD pipelines, and quantum-accelerated semiconductor inspection.", styles['TableJust'])
        ],
        [
            Paragraph("12", styles['TableCenter']),
            Paragraph("PSO1", styles['TableCenter']),
            Paragraph("Apply deep learning and image processing principles to model semiconductor wafer map patterns and design explainable visual feature attribution mechanisms.", styles['TableJust'])
        ],
        [
            Paragraph("13", styles['TableCenter']),
            Paragraph("PSO2", styles['TableCenter']),
            Paragraph("Understand the integration of privacy-preserving decentralized algorithms with post-hoc interpretability models for reliable industrial AI engineering.", styles['TableJust'])
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
        "Semiconductor manufacturing underpins nearly every modern electronic device, from mobile consumer electronics "
        "to mission-critical automotive and healthcare systems. Detecting wafer defects early during fabrication is vital "
        "to maximizing die yield, preventing downstream failures, and curtailing manufacturing overhead. However, conventional "
        "machine learning defect detection systems rely heavily on centralized data collection, requiring original equipment "
        "manufacturers (OEMs) and foundries to share proprietary wafer inspection maps—a practice strongly resisted due to "
        "intellectual property and trade secret concerns. Furthermore, state-of-the-art deep neural networks operate as opaque "
        "black boxes, providing negligible insight to process engineers as to why specific wafer patterns are flagged defective. "
        "This seminar presents a detailed review of the paper <b>“Demystifying Defects: Federated Learning and Explainable AI for "
        "Semiconductor Fault Detection”</b> by T. Patel, R. Murugan, G. Yenduri, R. H. Jhaveri, H. Snoussi, and T. Gaber, "
        "published in <i>IEEE Access</i>, Vol. 12, 2024. The paper introduces a privacy-preserving, transparent inspection "
        "framework combining decentralized federated training with post-hoc explainability."
    )
    story.append(Paragraph(abstract_p1, styles['AbstractBody']))
    story.append(Spacer(1, 18))

    abstract_p2 = (
        "The proposed framework distributes convolutional neural network backbones across ten client manufacturing stations, "
        "training models locally on private wafer image shards while ensuring raw data never leaves client boundaries. A central "
        "coordinator aggregates model weights via Federated Averaging (FedAvg) enhanced with calibrated Gaussian noise to enforce "
        "formal Differential Privacy against reconstruction attacks. Four deep learning architectures (ResNet152, DenseNet121, "
        "MobileNetV2, InceptionV3) were evaluated on the benchmark MixedWM38 dataset comprising over 38,000 grayscale wafer maps across "
        "38 defect classes. The ResNet152 federated model achieves a peak test accuracy of <b>98.78%</b>, outperforming prior deformable "
        "convolutional network baselines (DCNet, 93.20%) by nearly 5.6 percentage points. An integrated Explainable AI layer combining "
        "Gradient-weighted Class Activation Mapping (Grad-CAM) and Local Interpretable Model-agnostic Explanations (LIME) produces "
        "interpretable heatmaps and super-pixel attributions that confirm the model focuses on genuine physical defect clusters rather "
        "than background noise. This approach demonstrates that high detection accuracy, privacy preservation, and model transparency "
        "can be simultaneously achieved in modern semiconductor fabrication."
    )
    story.append(Paragraph(abstract_p2, styles['AbstractBody']))
    story.append(Spacer(1, 50))

    meta_abstract = [
        [
            Paragraph("<b>Keywords :</b> Semiconductor Manufacturing, Wafer Defect Detection, Federated Learning, Explainable AI (XAI), Differential Privacy, Grad-CAM, LIME.", ParagraphStyle('KW', fontName='Times-Roman', fontSize=10, leading=14))
        ],
        [
            Paragraph("<b>Seminar Presenter :</b> Joseph D Poonoly (Roll No: 36, Slot No: 27), S7 CSD, Federal Institute of Science and Technology (FISAT).", ParagraphStyle('SP', fontName='Times-Italic', fontSize=9.5, leading=13))
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

def main():
    styles = get_styles()

    # 1. Individual Mapping Form for Roll 36
    doc_map = SimpleDocTemplate(
        "1_FISAT_CSQ413_Seminar_Mapping_Form_Joseph_Poonoly_Roll36.pdf",
        pagesize=A4, leftMargin=40, rightMargin=40, topMargin=36, bottomMargin=36
    )
    doc_map.build(get_mapping_form_story(styles))
    print("Built 1_FISAT_CSQ413_Seminar_Mapping_Form_Joseph_Poonoly_Roll36.pdf")

    # 2. Individual Abstract for Roll 36
    doc_abs = SimpleDocTemplate(
        "2_Seminar_Abstract_Joseph_Poonoly_Roll36.pdf",
        pagesize=A4, leftMargin=40, rightMargin=40, topMargin=36, bottomMargin=36
    )
    doc_abs.build(get_abstract_story(styles))
    print("Built 2_Seminar_Abstract_Joseph_Poonoly_Roll36.pdf")

    # 3. Master Combined PDF for Roll 36
    from build_exact_plagiarism_pdf_roll36 import build_plagiarism_pdf
    build_plagiarism_pdf("3_Plagiarism_Detector_Report_Joseph_Poonoly_Roll36.pdf")

    # 4. Master 5-page PDF for Roll 36
    doc_all = SimpleDocTemplate(
        "Complete_Seminar_Submission_Joseph_Poonoly_Roll36.pdf",
        pagesize=A4, leftMargin=40, rightMargin=40, topMargin=32, bottomMargin=28
    )
    story_all = []
    story_all.extend(get_mapping_form_story(styles))
    story_all.append(PageBreak())
    story_all.extend(get_abstract_story(styles))
    story_all.append(PageBreak())
    from build_exact_plagiarism_pdf_roll36 import (
        create_header_drawing, create_card1_drawing, create_card2_drawing, create_card3_drawing,
        create_stats_bar, create_decorative_divider
    )
    # Plagiarism Page 1
    story_all.append(create_header_drawing())
    story_all.append(Spacer(1, 10))
    t_cards = Table([[create_card1_drawing(), create_card2_drawing(), create_card3_drawing()]], colWidths=[171.6, 171.6, 171.6])
    t_cards.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
    ]))
    story_all.append(t_cards)
    story_all.append(Spacer(1, 14))
    story_all.append(create_stats_bar())
    story_all.append(Spacer(1, 16))
    story_all.append(Paragraph("Plagiarism Sources", styles['SecTitle']))
    story_all.append(Spacer(1, 12))
    story_all.append(Paragraph("References", styles['SecTitle']))
    story_all.append(Spacer(1, 14))
    story_all.append(Paragraph("Document Content", styles['DocTitle']))
    story_all.append(Spacer(1, 4))
    from build_exact_plagiarism_pdf_roll36 import text_p1, text_p2
    story_all.append(Paragraph(text_p1, styles['ExactContent']))
    story_all.append(Spacer(1, 10))
    story_all.append(Paragraph("Page 1 of 2", styles['PageNum']))
    story_all.append(PageBreak())
    story_all.append(Paragraph(text_p2, styles['ExactContent']))
    story_all.append(Spacer(1, 25))
    story_all.append(create_decorative_divider())
    story_all.append(Spacer(1, 35))
    story_all.append(Paragraph("Page 2 of 2", styles['PageNum']))

    doc_all.build(story_all)
    print("Built Complete_Seminar_Submission_Joseph_Poonoly_Roll36.pdf")

if __name__ == "__main__":
    main()

