from django.core.management.base import BaseCommand

from ...models import Location


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # file_name = kwargs["file_name"]
        with open(f"static/docs/location_list.txt") as file:
            for row in file:
                location_name = row.lower().replace("\n", "")
                Location.objects.get_or_create(
                    location_name=location_name,
                )
        self.stdout.write(self.style.SUCCESS("list of locations added"))