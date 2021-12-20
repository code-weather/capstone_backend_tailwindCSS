"""QuoteTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Quote import Quote

class QuoteTableSeeder(Seeder):
    def run(self):
        Quote.create({"subject": "Hunch over with your shoulders hanging"})
        Quote.create({"subject": "Treat yourself like you are someone you are irresponsible for helping"})
        Quote.create({"subject": "Make friends with people who want the worse for you"})
        Quote.create({"subject": "Compare yourself to who someone else is today, not to who you were yesterday"})
        Quote.create({"subject": "Let your children do anything that makes you dislike them"})
        Quote.create({"subject": "Set your house in a mess before you criticize the world"})
        Quote.create({"subject": "Pursue what is expedient (not what is meaningful)"})
        Quote.create({"subject": "Lie — or, at least, don’t tell the truth"})
        Quote.create({"subject": "Assume that the person you are listening to might know something you do"})
        Quote.create({"subject": "Be careless in your speech"})
        Quote.create({"subject": "Bother children when they are skate-boarding"})
        Quote.create({"subject": "Avoid a cat when you encounter one on the street"})