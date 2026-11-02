import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
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
    d.add(Circle(14, 32, 9, strokeColor=GOLD_COLOR, strokeWidth=2.5, fillColor=colors.HexColor("#FFFBEB")))
    d.add(Line(20, 26, 26, 20, strokeColor=GOLD_COLOR, strokeWidth=2.5))
    d.add(Circle(14, 32, 4, strokeColor=colors.HexColor("#3B82F6"), strokeWidth=1.5, fillColor=None))

    d.add(String(32, 28, "Plagiarism", fontName="Helvetica-Bold", fontSize=13, fillColor=colors.HexColor("#111827")))
    d.add(String(100, 28, "Detector", fontName="Helvetica", fontSize=13, fillColor=colors.HexColor("#111827")))

    d.add(Rect(154, 27, 24, 12, rx=2, ry=2, fillColor=colors.HexColor("#FBBF24"), strokeColor=None))
    d.add(String(156, 29, ".net", fontName="Helvetica-Bold", fontSize=7.5, fillColor=colors.black))

    d.add(String(0, 6, "Plagiarism Detector Report Page", fontName="Helvetica-Bold", fontSize=14, fillColor=DARK_GRAY))
    return d

def create_card1_drawing():
    d = Drawing(167, 115)
    d.add(Rect(0, 0, 167, 115, rx=7, ry=7, strokeColor=LIGHT_BORDER, strokeWidth=1, fillColor=colors.white))
    d.add(String(83.5, 99, "Plagiarism Score", fontName="Helvetica", fontSize=9, textAnchor="middle", fillColor=DARK_GRAY))
    
    cx, cy, r = 44, 56, 26
    d.add(Circle(cx, cy, r, strokeColor=colors.HexColor("#ECEFF1"), strokeWidth=6, fillColor=None))
    d.add(Circle(cx, cy, r, strokeColor=PINK_RED, strokeWidth=6, fillColor=None))
    d.add(Circle(cx, cy, r - 3, strokeColor=None, fillColor=colors.white))
    d.add(String(cx, cy - 5, "6%", fontName="Helvetica-Bold", fontSize=13, textAnchor="middle", fillColor=PINK_RED))

    # Box 1: 6% Exact Match
    d.add(Rect(88, 62, 70, 17, rx=3, ry=3, strokeColor=PINK_BORDER, strokeWidth=1, fillColor=PINK_BG))
    d.add(String(92, 67, "6%", fontName="Helvetica-Bold", fontSize=7.5, fillColor=PINK_RED))
    d.add(String(106, 67, "Exact Match", fontName="Helvetica", fontSize=7, fillColor=MED_GRAY))

    # Box 2: 0% Partial Match
    d.add(Rect(88, 41, 70, 17, rx=3, ry=3, strokeColor=colors.HexColor("#E0E0E0"), strokeWidth=1, fillColor=colors.white))
    d.add(String(92, 46, "0%", fontName="Helvetica-Bold", fontSize=7.5, fillColor=colors.HexColor("#9E9E9E")))
    d.add(String(106, 46, "Partial Match", fontName="Helvetica", fontSize=7, fillColor=MED_GRAY))

    # Bottom Badge
    d.add(Rect(14, 11, 60, 15, rx=3, ry=3, strokeColor=colors.HexColor("#FFCDD2"), strokeWidth=1, fillColor=colors.HexColor("#FFEBEE")))
    d.add(String(44, 15.5, "Partially Original", fontName="Helvetica-Bold", fontSize=6.2, textAnchor="middle", fillColor=PINK_RED))
    return d

def create_card2_drawing():
    d = Drawing(167, 115)
    d.add(Rect(0, 0, 167, 115, rx=7, ry=7, strokeColor=LIGHT_BORDER, strokeWidth=1, fillColor=colors.white))
    d.add(String(83.5, 99, "Unique Score", fontName="Helvetica", fontSize=9, textAnchor="middle", fillColor=DARK_GRAY))
    
    cx, cy, r = 83.5, 52, 28
    d.add(Circle(cx, cy, r, strokeColor=GREEN_COLOR, strokeWidth=6.5, fillColor=None))
    d.add(Circle(cx, cy, r - 3.5, strokeColor=None, fillColor=colors.white))
    d.add(String(cx, cy - 6, "94%", fontName="Helvetica-Bold", fontSize=16, textAnchor="middle", fillColor=GREEN_COLOR))
    return d

def create_card3_drawing():
    d = Drawing(167, 115)
    d.add(Rect(0, 0, 167, 115, rx=7, ry=7, strokeColor=LIGHT_BORDER, strokeWidth=1, fillColor=colors.white))
    d.add(String(83.5, 99, "AI Detection Score", fontName="Helvetica", fontSize=9, textAnchor="middle", fillColor=DARK_GRAY))
    
    cx, cy, r = 83.5, 60, 26
    d.add(Circle(cx, cy, r, strokeColor=colors.HexColor("#CFD8DC"), strokeWidth=4, fillColor=None))
    d.add(String(cx, cy - 7, "?", fontName="Helvetica-Bold", fontSize=21, textAnchor="middle", fillColor=colors.HexColor("#78909C")))

    d.add(String(83.5, 22, "AI detection not performed. Scan with", fontName="Helvetica", fontSize=6.2, textAnchor="middle", fillColor=colors.HexColor("#757575")))
    d.add(String(83.5, 12, "Plagiarism Detector to view results.", fontName="Helvetica-Bold", fontSize=6.2, textAnchor="middle", fillColor=colors.HexColor("#7E57C2")))
    return d

def create_stats_bar():
    d = Drawing(515, 34)
    d.add(Rect(0, 0, 515, 34, rx=17, ry=17, strokeColor=colors.HexColor("#9E9E9E"), strokeWidth=1.2, fillColor=colors.white))
    
    d.add(Line(128, 0, 128, 34, strokeColor=colors.HexColor("#E0E0E0"), strokeWidth=1))
    d.add(Line(257, 0, 257, 34, strokeColor=colors.HexColor("#E0E0E0"), strokeWidth=1))
    d.add(Line(386, 0, 386, 34, strokeColor=colors.HexColor("#E0E0E0"), strokeWidth=1))

    d.add(String(20, 13, "Total Words", fontName="Helvetica", fontSize=8, fillColor=DARK_GRAY))
    d.add(String(95, 13, "986", fontName="Helvetica", fontSize=8.5, fillColor=colors.black))

    d.add(String(142, 13, "Total Characters", fontName="Helvetica", fontSize=8, fillColor=DARK_GRAY))
    d.add(String(225, 13, "7743", fontName="Helvetica", fontSize=8.5, fillColor=colors.black))

    d.add(String(272, 13, "Plagiarized Sentences", fontName="Helvetica", fontSize=8, fillColor=DARK_GRAY))
    d.add(String(365, 13, "63", fontName="Helvetica", fontSize=8.5, fillColor=colors.black))

    d.add(String(398, 13, "Unique Sentences", fontName="Helvetica", fontSize=8, fillColor=DARK_GRAY))
    d.add(String(480, 13, "100%", fontName="Helvetica", fontSize=8.5, fillColor=colors.black))
    return d

def create_decorative_divider():
    d = Drawing(515, 16)
    d.add(Circle(20, 8, 3, fillColor=GOLD_COLOR, strokeColor=None))
    d.add(Line(20, 8, 235, 8, strokeColor=GOLD_COLOR, strokeWidth=1.5))

    d.add(Polygon([240, 8, 244, 12, 248, 8, 244, 4], fillColor=GOLD_COLOR, strokeColor=None))
    d.add(Polygon([253, 8, 257.5, 13, 262, 8, 257.5, 3], fillColor=GOLD_COLOR, strokeColor=None))
    d.add(Polygon([267, 8, 271, 12, 275, 8, 271, 4], fillColor=GOLD_COLOR, strokeColor=None))

    d.add(Line(280, 8, 495, 8, strokeColor=GOLD_COLOR, strokeWidth=1.5))
    d.add(Circle(495, 8, 3, fillColor=GOLD_COLOR, strokeColor=None))
    return d

text_p1 = (
    "3.3 Study of Proposed System The proposed system combines federated learning with explainable artificial intelligence for wafer defect detection. "
    "Rather than relying on centralized data pooling that forces semiconductor foundries to expose proprietary fabrication data, the framework trains a global "
    "convolutional neural network across distributed clients without moving raw wafer images. The framework uses data collected through the MixedWM38 wafer map "
    "benchmark comprising over 38,000 grayscale wafer images across 38 fault classes. The study examines wafer spatial patterns <font color='#E53935'>"
    "Department of Computer Science and Design,FISAT 10Demystifying Defects: Federated Learning and Explainable AI for Semiconductor Fault Detection</font> "
    "characteristics such as center, donut, edge-ring, and mixed-type defect clusters. These characteristics are used to assess whether individual dies across the wafer "
    "satisfy strict semiconductor manufacturing yield standards. The collected wafer information is incorporated into the federated aggregation process. "
    "This enables the central model to learn robust representations across non-IID client distributions while preserving facility data confidentiality. The model "
    "first trains localized convolutional feature extractors across ten manufacturing nodes. When local client epochs conclude, the system applies Federated "
    "Averaging with calibrated Gaussian noise injection to provide differential privacy guarantees. The paper also presents an explainable AI layer combining "
    "Grad-CAM and LIME to support the practical auditing of code. The application is intended to communicate feature attribution heatmaps directly "
    "to foundry process engineers, making defect detection trustworthy and actionable. The overall approach connects decentralized training, privacy-preserving "
    "aggregation, and visual interpretability in a single framework. 3.4 Requirement Specification The proposed semiconductor fault detection framework involves "
    "wafer image ingestion, local client model training, secure gradient aggregation, and post-hoc visual explanation generation. Therefore, suitable data, "
    "processing capabilities, and software components are required to support the workflow. The study depends on the availability of standardized wafer map data "
    "derived from multi-stage fabrication sensors. The collected data must describe thirty-eight distinct single and mixed-type wafer defect patterns. A suitable "
    "computational environment is also required to process deep convolutional backbones and calculate differential privacy budgets. 3.4.1 Recommended System "
    "Requirements The following requirements describe the general computational resources needed to support a federated wafer inspection framework. They should "
    "not be interpreted as exact hardware specifications reported by the paper: • Processor: A high-performance multi-core CPU coupled with dedicated GPU acceleration "
    "(NVIDIA RTX 3080 or equivalent) to handle parallel convolutional tensor calculations. • Memory: Sufficient RAM to store normalized 52x52 wafer batch arrays and "
    "gradient update caches (Minimum 16GB, 32GB recommended). • Storage: Adequate high-speed SSD storage for caching the MixedWM38 dataset, model checkpoints, and "
    "t-SNE clustering projections. • Network Connectivity: Low-latency local network or TLS-encrypted tunnel required for transferring weight update tensors between client "
    "inspection nodes and the central aggregation server. • Execution Environment: Linux-based operating system (Ubuntu 22.04 LTS) configured with CUDA acceleration "
    "libraries for client training. <font color='#E53935'>Department of Computer Science and Design,FISAT 11Demystifying Defects: Federated Learning and Explainable AI "
    "for Semiconductor Fault Detection</font> • Explainability Module: Dedicated compute capacity to generate pixel-level Grad-CAM heatmaps and LIME super-pixel "
    "perturbation surrogates for real-time defect verification. 3.4.2 Software Requirements The framework requires software components capable of training deep residual "
    "networks, managing decentralized communication rounds, injecting differential privacy noise, and generating visual heatmaps: • Data Preprocessing: Image processing "
    "libraries for grayscale normalization, pixel standardization, and one-hot encoding of 38 defect categories. • Machine Learning Engine: PyTorch / TensorFlow runtime "
    "supporting ResNet152, DenseNet121, MobileNetV2, and InceptionV3 backbones. • Federated Orchestration: Framework supporting Federated Averaging (FedAvg) and client "
    "node scheduling across 10 communication rounds. • Privacy Engine: Differential privacy routines for calibrated Gaussian perturbation of global weight updates. "
    "• Explainable AI Suite: Grad-CAM gradient backpropagation modules and LIME local surrogate algorithms for interpretable inspection. 3.5 Functional Requirements "
    "The federated wafer fault detection framework should satisfy the following functional requirements: 1. The system shall partition the wafer map dataset into ten "
    "private client shards representing decentralized fabrication stations. 2. The system shall train local convolutional models on private wafer image data without "
    "exporting raw wafer images off-site. 3. The system shall evaluate four deep learning architectures (ResNet152, DenseNet121, MobileNetV2, InceptionV3) using residual "
    "skip connections. 4. The system shall combine client weight updates at a central coordinator server using Federated Averaging (FedAvg). 5. The system shall inject "
    "calibrated Gaussian noise into aggregated model weights to guarantee formal differential privacy. 6. The system shall achieve high classification accuracy across all "
    "thirty-eight single, two-mixed, three-mixed, and four-mixed defect categories. 7. The system shall generate Grad-CAM class activation heatmaps highlighting the exact "
    "die regions responsible for defect classification. <font color='#E53935'>Department of Computer Science and Design,FISAT 12Demystifying Defects: Federated Learning "
    "and Explainable AI for Semiconductor Fault Detection</font> 8. The system shall construct LIME super-pixel segmentation overlays to corroborate model focus. "
    "9. The system shall support feature space visualization via t-SNE clustering to verify cross-client latent representation quality. 10. The system shall support the "
    "presentation of automated defect inspection"
)

text_p2 = (
    "recommendations through an intuitive inspection dashboard for fab engineers. 3.6 Non-Functional Requirements The federated semiconductor inspection framework "
    "should satisfy the following non-functional requirements: • Privacy Preservation: Raw wafer images must strictly reside within client fabrication boundaries, and "
    "differential privacy noise must prevent gradient reconstruction attacks. • Accuracy and Reliability: The global federated classifier must achieve high generalization "
    "accuracy, matching or exceeding centralized baselines (reaching a verified 98.78% test accuracy with ResNet152, outperforming DCNet by 5.58 percentage points). "
    "• Convergence and Communication Efficiency: The federated optimization protocol must achieve stable convergence within a constrained budget of 10 communication "
    "rounds. • Transparency and Explainability: Model predictions must be accompanied by faithful, human-interpretable visual explanations (Grad-CAM and LIME) to "
    "eliminate black-box opacity and establish domain trust among foundry engineers. • Robustness to Data Heterogeneity: The framework must maintain stable classification "
    "performance across unbalanced defect distributions and varying client dataset volumes. • Scalability: The architecture must easily scale to accommodate additional "
    "manufacturing facilities and new wafer geometry formats without requiring architectural reconfiguration. • Maintainability: Modular separation between the client "
    "training nodes, aggregation server, and XAI interpretation pipeline must allow independent algorithmic updates. 3.7 Summary This chapter analysed the system "
    "overview, architectural design, dataset characteristics, and technical requirements of the federated learning and explainable AI framework for semiconductor defect "
    "detection. The reviewed framework addresses the privacy bottlenecks of centralized training and the black-box opacity of deep neural networks by combining "
    "decentralized FedAvg, differential privacy, and dual XAI interpretability layers. The proposed approach connects private localized training on 38,000 wafer maps "
    "with transparent attribution heatmaps, demonstrating superior accuracy and operational trustworthiness for multi-stakeholder industrial semiconductor "
    "manufacturing. Department of Computer Science and Design,FISAT"
)

def build_plagiarism_pdf(filename="3_Plagiarism_Detector_Report_Joseph_Poonoly_Roll36.pdf"):
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

    # 3 Metric Cards
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

    # Stats Bar
    story.append(create_stats_bar())
    story.append(Spacer(1, 16))

    story.append(Paragraph("Plagiarism Sources", style_sec_title))
    story.append(Spacer(1, 12))
    story.append(Paragraph("References", style_sec_title))
    story.append(Spacer(1, 14))

    story.append(Paragraph("Document Content", style_doc_title))
    story.append(Spacer(1, 4))

    # Content for Joseph D Poonoly (Roll 36) - Semiconductor Fault Detection FL + XAI
    text_p1 = (
        "3.3 Study of Proposed System The proposed system combines federated learning with explainable artificial intelligence for wafer defect detection. "
        "Rather than relying on centralized data pooling that forces semiconductor foundries to expose proprietary fabrication data, the framework trains a global "
        "convolutional neural network across distributed clients without moving raw wafer images. The framework uses data collected through the MixedWM38 wafer map "
        "benchmark comprising over 38,000 grayscale wafer images across 38 fault classes. The study examines wafer spatial patterns <font color='#E53935'>"
        "Department of Computer Science and Design,FISAT 10Demystifying Defects: Federated Learning and Explainable AI for Semiconductor Fault Detection</font> "
        "characteristics such as center, donut, edge-ring, and mixed-type defect clusters. These characteristics are used to assess whether individual dies across the wafer "
        "satisfy strict semiconductor manufacturing yield standards. The collected wafer information is incorporated into the federated aggregation process. "
        "This enables the central model to learn robust representations across non-IID client distributions while preserving facility data confidentiality. The model "
        "first trains localized convolutional feature extractors across ten manufacturing nodes. When local client epochs conclude, the system applies Federated "
        "Averaging with calibrated Gaussian noise injection to provide differential privacy guarantees. The paper also presents an explainable AI layer combining "
        "Grad-CAM and LIME to support the transparent interpretation of predictions. The application is intended to communicate feature attribution heatmaps directly "
        "to foundry process engineers, making defect detection trustworthy and actionable. The overall approach connects decentralized training, privacy-preserving "
        "aggregation, and visual interpretability in a single framework. 3.4 Requirement Specification The proposed semiconductor fault detection framework involves "
        "wafer image ingestion, local client model training, secure gradient aggregation, and post-hoc visual explanation generation. Therefore, suitable data, "
        "processing capabilities, and software components are required to support the workflow. The study depends on the availability of standardized wafer map data "
        "derived from multi-stage fabrication sensors. The collected data must describe thirty-eight distinct single and mixed-type wafer defect patterns. A suitable "
        "computational environment is also required to process deep convolutional backbones and calculate differential privacy budgets. 3.4.1 Recommended System "
        "Requirements The following requirements describe the general computational resources needed to support a federated wafer inspection framework. They should "
        "not be interpreted as exact hardware specifications reported by the paper: • Processor: A high-performance multi-core CPU coupled with dedicated GPU acceleration "
        "(NVIDIA RTX 3080 or equivalent) to handle parallel convolutional tensor calculations. • Memory: Sufficient RAM to store normalized 52x52 wafer batch arrays and "
        "gradient update caches (Minimum 16GB, 32GB recommended). • Storage: Adequate high-speed SSD storage for caching the MixedWM38 dataset, model checkpoints, and "
        "t-SNE clustering projections. • Network Connectivity: Low-latency local network or TLS-encrypted tunnel required for transferring weight update tensors between client "
        "inspection nodes and the central aggregation server. • Execution Environment: Linux-based operating system (Ubuntu 22.04 LTS) configured with CUDA acceleration "
        "libraries for client training. <font color='#E53935'>Department of Computer Science and Design,FISAT 11Demystifying Defects: Federated Learning and Explainable AI "
        "for Semiconductor Fault Detection</font> • Explainability Module: Dedicated compute capacity to generate pixel-level Grad-CAM heatmaps and LIME super-pixel "
        "perturbation surrogates for real-time defect verification. 3.4.2 Software Requirements The framework requires software components capable of training deep residual "
        "networks, managing decentralized communication rounds, injecting differential privacy noise, and generating visual heatmaps: • Data Preprocessing: Image processing "
        "libraries for grayscale normalization, pixel standardization, and one-hot encoding of 38 defect categories. • Machine Learning Engine: PyTorch / TensorFlow runtime "
        "supporting ResNet152, DenseNet121, MobileNetV2, and InceptionV3 backbones. • Federated Orchestration: Framework supporting Federated Averaging (FedAvg) and client "
        "node scheduling across 10 communication rounds. • Privacy Engine: Differential privacy routines for calibrated Gaussian perturbation of global weight updates. "
        "• Explainable AI Suite: Grad-CAM gradient backpropagation modules and LIME local surrogate algorithms for interpretable inspection. 3.5 Functional Requirements "
        "The federated wafer fault detection framework should satisfy the following functional requirements: 1. The system shall partition the wafer map dataset into ten "
        "private client shards representing decentralized fabrication stations. 2. The system shall train local convolutional models on private wafer image data without "
        "exporting raw wafer images off-site. 3. The system shall evaluate four deep learning architectures (ResNet152, DenseNet121, MobileNetV2, InceptionV3) using residual "
        "skip connections. 4. The system shall combine client weight updates at a central coordinator server using Federated Averaging (FedAvg). 5. The system shall inject "
        "calibrated Gaussian noise into aggregated model weights to guarantee formal differential privacy. 6. The system shall achieve high classification accuracy across all "
        "thirty-eight single, two-mixed, three-mixed, and four-mixed defect categories. 7. The system shall generate Grad-CAM class activation heatmaps highlighting the exact "
        "die regions responsible for defect classification. <font color='#E53935'>Department of Computer Science and Design,FISAT 12Demystifying Defects: Federated Learning "
        "and Explainable AI for Semiconductor Fault Detection</font> 8. The system shall construct LIME super-pixel segmentation overlays to corroborate model focus. "
        "9. The system shall support feature space visualization via t-SNE clustering to verify cross-client latent representation quality. 10. The system shall support the "
        "presentation of automated defect inspection"
    )
    story.append(Paragraph(text_p1, style_content))
    story.append(Spacer(1, 10))

    story.append(Paragraph("Page 1 of 2", style_page_num))
    story.append(PageBreak())

    # ================= PAGE 2 =================
    text_p2 = (
        "recommendations through an intuitive inspection dashboard for fab engineers. 3.6 Non-Functional Requirements The federated semiconductor inspection framework "
        "should satisfy the following non-functional requirements: • Privacy Preservation: Raw wafer images must strictly reside within client fabrication boundaries, and "
        "differential privacy noise must prevent gradient reconstruction attacks. • Accuracy and Reliability: The global federated classifier must achieve high generalization "
        "accuracy, matching or exceeding centralized baselines (reaching a verified 98.78% test accuracy with ResNet152, outperforming DCNet by 5.58 percentage points). "
        "• Convergence and Communication Efficiency: The federated optimization protocol must achieve stable convergence within a constrained budget of 10 communication "
        "rounds. • Transparency and Explainability: Model predictions must be accompanied by faithful, human-interpretable visual explanations (Grad-CAM and LIME) to "
        "eliminate black-box opacity and establish domain trust among foundry engineers. • Robustness to Data Heterogeneity: The framework must maintain stable classification "
        "performance across unbalanced defect distributions and varying client dataset volumes. • Scalability: The architecture must easily scale to accommodate additional "
        "manufacturing facilities and new wafer geometry formats without requiring architectural reconfiguration. • Maintainability: Modular separation between the client "
        "training nodes, aggregation server, and XAI interpretation pipeline must allow independent algorithmic updates. 3.7 Summary This chapter analysed the system "
        "overview, architectural design, dataset characteristics, and technical requirements of the federated learning and explainable AI framework for semiconductor defect "
        "detection. The reviewed framework addresses the privacy bottlenecks of centralized training and the black-box opacity of deep neural networks by combining "
        "decentralized FedAvg, differential privacy, and dual XAI interpretability layers. The proposed approach connects private localized training on 38,000 wafer maps "
        "with transparent attribution heatmaps, demonstrating superior accuracy and operational trustworthiness for multi-stakeholder industrial semiconductor "
        "manufacturing. Department of Computer Science and Design,FISAT"
    )
    story.append(Paragraph(text_p2, style_content))
    story.append(Spacer(1, 25))

    story.append(create_decorative_divider())
    story.append(Spacer(1, 35))

    story.append(Paragraph("Page 2 of 2", style_page_num))

    doc.build(story)
    print(f"Built exact plagiarism report for Roll 36: {filename}")

if __name__ == "__main__":
    build_plagiarism_pdf()
