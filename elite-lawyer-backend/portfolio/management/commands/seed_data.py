from django.core.management.base import BaseCommand
from portfolio.models import Achievement, Testimonial, Recognition

class Command(BaseCommand):
    help = "Seed portfolio data (achievements, testimonials, recognitions)"

    def handle(self, *args, **kwargs):
        achievements = [
            {"metric": "30+", "label": "Years of Practice", "description": "Extensive experience..."},
            {"metric": "$2B+", "label": "In Transactions", "description": "Successfully structured..."},
            {"metric": "98%", "label": "Success Rate", "description": "Favorable outcomes..."},
            {"metric": "200+", "label": "Corporate Clients", "description": "From Fortune 500..."},
        ]

        testimonials = [
            {"quote": "Richard's strategic insight...", "author": "CEO, Leading Financial Institution", "role": "Banking & Finance"},
            {"quote": "Exceptional legal acumen...", "author": "General Counsel, Multinational Corp", "role": "Corporate Advisory"},
            {"quote": "In matters requiring...", "author": "Chairman, Private Equity Firm", "role": "M&A Transaction"},
        ]

        recognitions = [
            {"title": "Leading Individual (Corporate/M&A)", "organization": "Chambers & Partners"},
            {"title": "Hall of Fame Member", "organization": "Legal 500"},
            {"title": "Distinguished Fellow", "organization": "International Bar Association"},
            {"title": "Senior Advocate Recognition", "organization": "East African Law Society"},
        ]

        for a in achievements:
            Achievement.objects.get_or_create(**a)

        for t in testimonials:
            Testimonial.objects.get_or_create(**t)

        for r in recognitions:
            Recognition.objects.get_or_create(**r)

        self.stdout.write(self.style.SUCCESS("Seeded portfolio data successfully!"))
