from unittest import TestCase
import container
from app.domain.model import Property, Area


class WorldServiceTest(TestCase):
    def test_should_add_properties(self):
        property = Property(
            title='foo',
            x=100,
            y=100,
            price=120000,
            beds=2,
            baths=2,
            description='some bar',
            squareMeters=200,
        )

        container.world_service.add_property(property)

        self.assertEqual(property.provinces, ['Scavy'])

    def test_should_search_properties(self):
        property = Property(
            title='foo',
            x=500,
            y=600,
            price=120000,
            beds=2,
            baths=2,
            description='some bar',
            squareMeters=200,
        )

        container.world_service.add_property(property)

        self.assertEqual(property.provinces, ['Gode', 'Ruja'])

        property.x = 520
        container.world_service.add_property(property)

        properties = container.world_service.get_properties(Area(0, 1000, 600, 500))

        self.assertEqual(len(properties), 2)

    def test_should_validate_property(self):
        with self.assertRaises(AssertionError):
            property = Property(
                title='foo',
                x=1500,
                y=600,
                price=120000,
                beds=2,
                baths=2,
                description='some bar',
                squareMeters=200,
            )

        with self.assertRaises(AssertionError):
            property = Property(
                title='foo',
                x=1300,
                y=1200,
                price=120000,
                beds=2,
                baths=2,
                description='some bar',
                squareMeters=200,
            )
