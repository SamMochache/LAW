from django.core.management.base import BaseCommand
from portfolio.models import (
    PracticeArea, 
    Experience, 
    Credential, 
    Philosophy, 
    Achievement, 
    Testimonial, 
    Recognition
)

class Command(BaseCommand):
    help = "Seed portfolio data with premium, high-end content"

    def handle(self, *args, **kwargs):
        # Clear existing data
        self.stdout.write("Clearing existing data...")
        PracticeArea.objects.all().delete()
        Experience.objects.all().delete()
        Credential.objects.all().delete()
        Philosophy.objects.all().delete()
        Achievement.objects.all().delete()
        Testimonial.objects.all().delete()
        Recognition.objects.all().delete()

        # PRACTICE AREAS - Elite specializations
        practice_areas = [
            {
                "title": "Mergers & Acquisitions",
                "description": "Strategic counsel on complex cross-border transactions, including hostile takeovers, leveraged buyouts, and corporate restructuring for multinational corporations and private equity firms."
            },
            {
                "title": "Capital Markets & Securities",
                "description": "Advising on IPOs, private placements, debt offerings, and regulatory compliance for public companies. Extensive experience with SEC filings, corporate governance, and shareholder activism defense."
            },
            {
                "title": "Commercial Litigation & Arbitration",
                "description": "Representing corporations and high-net-worth individuals in high-stakes commercial disputes, international arbitration, and white-collar defense matters before courts and tribunals."
            },
            {
                "title": "Private Equity & Venture Capital",
                "description": "Structuring fund formations, growth capital transactions, and exit strategies for leading investment firms. Counsel to both GPs and LPs on complex fund documentation and regulatory matters."
            },
            {
                "title": "Banking & Structured Finance",
                "description": "Advising financial institutions on syndicated lending, project finance, securitization transactions, and regulatory compliance across multiple jurisdictions in East Africa and beyond."
            },
            {
                "title": "Tax & Transfer Pricing",
                "description": "Strategic tax planning for multinational enterprises, transfer pricing optimization, advance tax rulings, and representation in high-value tax disputes with revenue authorities."
            },
        ]

        for area in practice_areas:
            PracticeArea.objects.create(**area)
        self.stdout.write(self.style.SUCCESS(f"✓ Created {len(practice_areas)} practice areas"))

        # EXPERIENCE - High-profile, confidential matters
        experiences = [
            {
                "title": "Cross-Border Acquisition - Regional Telecommunications Leader",
                "summary": "Lead counsel in $850M acquisition of East African telecommunications infrastructure assets. Negotiated complex regulatory approvals across five jurisdictions, structured tax-efficient holdco arrangements, and coordinated multi-jurisdictional due diligence teams."
            },
            {
                "title": "Hostile Takeover Defense - Listed Financial Institution",
                "summary": "Successfully defended a leading regional bank against unsolicited takeover attempt. Deployed poison pill defense mechanisms, advised board on fiduciary duties, and negotiated white knight transaction preserving shareholder value."
            },
            {
                "title": "Sovereign Wealth Fund - Infrastructure Investment",
                "summary": "Structured $1.2B co-investment by Middle Eastern sovereign wealth fund in East African port and logistics infrastructure. Negotiated concession agreements, advised on political risk mitigation, and established governance frameworks."
            },
            {
                "title": "Private Equity Carve-Out - Manufacturing Conglomerate",
                "summary": "Advised international PE firm on $420M carve-out of manufacturing division from publicly-listed conglomerate. Structured management equity incentives, negotiated transitional service agreements, and managed complex separation matters."
            },
            {
                "title": "International Arbitration - Energy Sector Dispute",
                "summary": "Represented multinational energy company in LCIA arbitration concerning breach of power purchase agreement. Successfully obtained $180M damages award and enforcement across multiple jurisdictions."
            },
            {
                "title": "IPO and Dual Listing - Technology Company",
                "summary": "Lead counsel for first dual-listing of African technology company on NSE and LSE. Coordinated with international underwriters, managed regulatory approvals, and structured cornerstone investor participation in oversubscribed $300M offering."
            },
        ]

        for exp in experiences:
            Experience.objects.create(**exp)
        self.stdout.write(self.style.SUCCESS(f"✓ Created {len(experiences)} selected experiences"))

        # CREDENTIALS - Elite education and qualifications
        credentials = [
            {
                "title": "Bachelor of Laws (LLB), First Class Honours",
                "institution": "University of Nairobi",
                "year": "1992"
            },
            {
                "title": "Master of Laws (LLM) - Corporate & Commercial Law",
                "institution": "London School of Economics and Political Science",
                "year": "1995"
            },
            {
                "title": "Senior Advocate of the High Court of Kenya",
                "institution": "Chief Justice of Kenya",
                "year": "2008"
            },
            {
                "title": "Certificate in International Arbitration",
                "institution": "Chartered Institute of Arbitrators, London",
                "year": "1998"
            },
            {
                "title": "Advanced Management Program",
                "institution": "Harvard Business School",
                "year": "2012"
            },
            {
                "title": "Admitted to Practice",
                "institution": "High Court of Kenya, Court of Appeal, Supreme Court",
                "year": "1993"
            },
        ]

        for cred in credentials:
            Credential.objects.create(**cred)
        self.stdout.write(self.style.SUCCESS(f"✓ Created {len(credentials)} credentials"))

        # PHILOSOPHY - Sophisticated legal philosophy
        philosophy_text = """The practice of law at this level transcends technical expertise—it demands strategic foresight, 
commercial acumen, and an unwavering commitment to client objectives. Every engagement is approached with three 
fundamental principles: understand the business context deeply, anticipate obstacles before they materialize, and 
structure solutions that create enduring value.

Elite legal counsel is not merely about navigating the law, but about shaping outcomes. It requires the ability 
to synthesize complex regulatory frameworks across jurisdictions, negotiate from positions of strength, and maintain 
absolute discretion in matters of commercial sensitivity.

The relationship between advocate and client is built on trust earned through consistent delivery of exceptional 
results. This trust is honored through rigorous preparation, intellectual honesty, and the courage to provide 
candid counsel—even when that counsel challenges conventional thinking.

In an era of increasing complexity and cross-border commerce, sophisticated legal guidance has never been more critical. 
The difference between good counsel and exceptional counsel often determines whether a transaction succeeds or fails, 
whether a dispute is resolved favorably or becomes a protracted liability, and whether a company's strategic objectives 
are achieved or compromised."""

        Philosophy.objects.create(body=philosophy_text)
        self.stdout.write(self.style.SUCCESS("✓ Created legal philosophy"))

        # ACHIEVEMENTS - Impressive metrics
        achievements = [
            {
                "metric": "32+",
                "label": "Years of Practice",
                "description": "Three decades advising on the most complex legal matters across East Africa and internationally",
                "order": 1
            },
            {
                "metric": "$8.5B+",
                "label": "Transaction Value",
                "description": "Cumulative value of M&A, capital markets, and financing transactions successfully closed",
                "order": 2
            },
            {
                "metric": "97%",
                "label": "Success Rate",
                "description": "Favorable outcomes in litigation, arbitration, and contentious regulatory matters",
                "order": 3
            },
            {
                "metric": "250+",
                "label": "Corporate Clients",
                "description": "Multinational corporations, financial institutions, and sovereign entities served",
                "order": 4
            },
        ]

        for achievement in achievements:
            Achievement.objects.create(**achievement)
        self.stdout.write(self.style.SUCCESS(f"✓ Created {len(achievements)} achievements"))

        # TESTIMONIALS - Elite client feedback (confidential, anonymous)
        testimonials = [
            {
                "quote": "Richard's strategic guidance was instrumental in navigating the most complex cross-border transaction our firm has undertaken. His ability to anticipate regulatory obstacles and structure creative solutions exceeded all expectations.",
                "author": "Managing Partner",
                "role": "Global Private Equity Firm",
                "order": 1,
                "is_active": True
            },
            {
                "quote": "In three decades of executing major transactions across Africa, I have rarely encountered counsel who combines Richard's technical mastery with such profound commercial awareness. He doesn't just solve legal problems—he advances business objectives.",
                "author": "Chief Executive Officer",
                "role": "Multinational Financial Institution",
                "order": 2,
                "is_active": True
            },
            {
                "quote": "When facing a hostile takeover attempt, we needed counsel who could operate under intense pressure with absolute discretion. Richard's strategic defense and flawless execution protected over $2 billion in shareholder value.",
                "author": "Chairman of the Board",
                "role": "Listed Banking Group",
                "order": 3,
                "is_active": True
            },
            {
                "quote": "Richard's representation in our international arbitration was nothing short of masterful. His preparation, advocacy, and tactical judgment resulted in a complete vindication of our position and substantial damages recovery.",
                "author": "General Counsel",
                "role": "Energy Sector Multinational",
                "order": 4,
                "is_active": True
            },
            {
                "quote": "As lead counsel for our IPO and dual-listing, Richard coordinated seamlessly with international advisors while ensuring flawless compliance across multiple jurisdictions. The transaction's success reflects his exceptional capabilities.",
                "author": "Founder & CEO",
                "role": "Technology Unicorn",
                "order": 5,
                "is_active": True
            },
            {
                "quote": "Richard understands that legal advice must serve broader strategic objectives. His counsel consistently demonstrates the rare combination of deep technical expertise and sophisticated business judgment that defines elite advocacy.",
                "author": "Senior Investment Director",
                "role": "Sovereign Wealth Fund",
                "order": 6,
                "is_active": True
            },
        ]

        for testimonial in testimonials:
            Testimonial.objects.create(**testimonial)
        self.stdout.write(self.style.SUCCESS(f"✓ Created {len(testimonials)} testimonials"))

        # RECOGNITIONS - Prestigious awards and rankings
        recognitions = [
            {
                "title": "Band 1 - Leading Individual (Corporate/M&A)",
                "organization": "Chambers & Partners",
                "year": "2024",
                "order": 1,
                "is_active": True
            },
            {
                "title": "Leading Lawyer - Capital Markets",
                "organization": "Legal 500 EMEA",
                "year": "2024",
                "order": 2,
                "is_active": True
            },
            {
                "title": "Hall of Fame - Corporate and Commercial Law",
                "organization": "Legal 500",
                "year": "2023",
                "order": 3,
                "is_active": True
            },
            {
                "title": "Lifetime Achievement Award",
                "organization": "East African Law Society",
                "year": "2022",
                "order": 4,
                "is_active": True
            },
            {
                "title": "Distinguished Fellow",
                "organization": "International Bar Association",
                "year": "2021",
                "order": 5,
                "is_active": True
            },
            {
                "title": "Senior Counsel Recognition",
                "organization": "Chief Justice of Kenya",
                "year": "2008",
                "order": 6,
                "is_active": True
            },
            {
                "title": "Dealmaker of the Year - East Africa",
                "organization": "African Legal Awards",
                "year": "2020",
                "order": 7,
                "is_active": True
            },
            {
                "title": "Top Ranked - Banking & Finance",
                "organization": "IFLR1000",
                "year": "2024",
                "order": 8,
                "is_active": True
            },
            {
                "title": "Notable Practitioner - International Arbitration",
                "organization": "Who's Who Legal",
                "year": "2024",
                "order": 9,
                "is_active": True
            },
            {
                "title": "Advisory Board Member",
                "organization": "Harvard Law School Africa Initiative",
                "year": "2019",
                "order": 10,
                "is_active": True
            },
        ]

        for recognition in recognitions:
            Recognition.objects.create(**recognition)
        self.stdout.write(self.style.SUCCESS(f"✓ Created {len(recognitions)} recognitions"))

        # Success summary
        self.stdout.write(self.style.SUCCESS("\n" + "="*60))
        self.stdout.write(self.style.SUCCESS("DATABASE SEEDED SUCCESSFULLY"))
        self.stdout.write(self.style.SUCCESS("="*60))
        self.stdout.write(self.style.SUCCESS(f"Practice Areas:  {PracticeArea.objects.count()}"))
        self.stdout.write(self.style.SUCCESS(f"Experiences:     {Experience.objects.count()}"))
        self.stdout.write(self.style.SUCCESS(f"Credentials:     {Credential.objects.count()}"))
        self.stdout.write(self.style.SUCCESS(f"Philosophy:      {Philosophy.objects.count()}"))
        self.stdout.write(self.style.SUCCESS(f"Achievements:    {Achievement.objects.count()}"))
        self.stdout.write(self.style.SUCCESS(f"Testimonials:    {Testimonial.objects.count()}"))
        self.stdout.write(self.style.SUCCESS(f"Recognitions:    {Recognition.objects.count()}"))
        self.stdout.write(self.style.SUCCESS("="*60 + "\n"))