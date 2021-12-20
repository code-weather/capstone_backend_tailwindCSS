"""CreateQuotesTable Migration."""

from masoniteorm.migrations import Migration


class CreateQuotesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("quotes") as table:
            table.increments("id")
            table.string("subject")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("quotes")
