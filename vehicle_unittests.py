from unittest import TestCase, main
from vehicle import *

class Tests(TestCase):
    '''This class provides tests for vehicle module'''

    def test_vehicle(self):
        v1 = Vehicle("Zorith", 2)
        self.assertEqual(str(v1), "Zorith holds 2: [], free 2")
        self.assertTrue(v1.is_empty())
    
        p1 = Passenger('Arman')
        p2 = Passenger('Armana')
        self.assertEqual(str(p1), "Arman is passenger of ...")
        self.assertTrue(v1.add_passenger(p1))
        self.assertEqual(p1.place, v1)
        self.assertEqual(p1._Passenger__place, v1)
        self.assertEqual(str(p1), "Arman is passenger of Zorith")
        self.assertFalse(v1.add_passenger(p1))
        self.assertTrue(v1.add_passenger(p2))

        p3 = Passenger("Arcana")
        self.assertFalse(v1.add_passenger(p3))
        self.assertEqual(str(v1), "Zorith holds 2: ['Arman', 'Armana'], free 0")
        # can remove the most recent passenger
        self.assertEqual(v1.remove_passenger(), p2)
        self.assertEqual(str(v1), "Zorith holds 2: ['Arman'], free 1")
        self.assertTrue(v1.add_passenger(p3))

    def test_comparability(self):
        path = "Lviv - Stari Kuty"
        v1 = Vehicle("Zorith", 2)
        v2 = Bus("Bus", 20, path)
        p2 = Passenger('Armana')
        p3 = Passenger("Arcana")
        self.assertFalse(v2.remove_passenger())
        self.assertTrue(v2.add_passenger(p2))
        self.assertEqual(str(v2), 'Bus holds 20: [\'Armana\'], free 19')
        self.assertEqual(v1.remove_passenger(), (p2, 'Bus is empty!'))
        self.assertEqual(v2, Bus('Bus', 20, path))
        self.assertNotEqual(v2, Bus('Bus', 20, 'Lviv - Tuziliv'))
        self.assertNotEqual(v2, v1)
        self.assertNotEqual(v2, 'Bus')


    def test_buggy(self):
        b1 = Buggy("ADC Buggy")
        p4 = Driver("Driver")
        self.assertTrue(b1.add_passenger(p4))
        self.assertEqual(p4.place, b1)
        self.assertEqual(str(b1), 'ADC Buggy holds 1: [\'Driver\'], free 0')

        b1.start_pushing()
        self.assertFalse(b1.remove_passenger())
        b1.stop_pushing()

        self.assertEqual(b1.remove_passenger(), p4)
        self.assertFalse(b1.remove_passenger())

        b2 = Buggy("SD Buggy")
        b3 = Buggy("DC Buggy")
        self.assertEqual(b2, Buggy("SD Buggy"))
        self.assertNotEqual(b2, b3)
        self.assertEqual(Buggy.buggy_count(), 4)

        garage = set()
        v1 = Vehicle("Zorith", 2)
        self.assertTrue(v1 not in garage)
        garage.add(v1)
        self.assertTrue(v1 in garage)
        self.assertTrue(b1 not in garage)
        garage.add(b1)
        self.assertTrue(b1 in garage)
        garage.remove(b1)
        self.assertTrue(b1 not in garage)

        print('Done')

if __name__ == '__main__':
    main(argv=[''], verbosity=2, exit=False)
