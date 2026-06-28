from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(founder):

    filename = f"reports/{founder['name']}_report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>FoundrAI Founder Report</b>", styles["Title"]))

    story.append(Paragraph(f"Name: {founder['name']}", styles["Normal"]))

    story.append(Paragraph(f"Founder Score: {founder['score']:.2f}", styles["Normal"]))

    story.append(Paragraph(f"AI Recommendation:", styles["Heading2"]))

    story.append(Paragraph(founder["ai_response"], styles["Normal"]))

    doc.build(story)

    return filename