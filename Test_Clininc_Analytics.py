import unittest
from Clinic_Analytics import Clinic, Darmangar, Moraje, Jalase

class TestClinic_Analytics(unittest.TestCase) :

    @classmethod
    def setUpClass(self): 
        print("setup class started")
        self.clinic = Clinic("Clinic A")
        self.darmangar = Darmangar(self.clinic, "Dr. Due", "Rogan", "D001", 9102587964, "kardarnmani", 5)
        self.moraje = Moraje(self.clinic, self.darmangar, "Goe", "Antimuli", "M001", 9135698741, "cp","Jame vije")

        self.darmangar.sabt_darmangar()
        self.moraje.sabt_moraje()

        self.j_1 = Jalase(self.clinic, self.darmangar, self.moraje,True,True)
        self.j_2 = Jalase(self.clinic, self.darmangar, self.moraje,True,False)
        self.j_3 = Jalase(self.clinic, self.darmangar, self.moraje,False,True)

        self.j_1.sabt_jalaseh()
        self.j_2.sabt_jalaseh()
        self.j_3.sabt_jalaseh()
    
    @classmethod
    def tearDownClass(self):
        print("teardown class ended")

    def test_Moraje_sabt_moraje(self):
        print("test_Moraje_sabt_moraje")
        self.assertIn(self.moraje.code, self.clinic.morajein)
        self.assertEqual(self.clinic.morajein[self.moraje.code], "Goe Antimuli")

    def test_Moraje_tedad_jalasat_va_gheibat(self):
        print("test_Moraje_tedad_jalasat_va_gheibat")
        self.assertEqual(self.moraje.tedad_jalasat(), 1)
        self.assertEqual(self.moraje.tedad_gheibat(), 1)

    def test_Moraje_hazineh_pardakhti(self):
        print("test_Moraje_hazineh_pardakhti")
        self.assertEqual(self.moraje.hazineh_pardakhti(self.clinic, self.darmangar), 900000)

    def test_Darmangar_tedad_gheibat(self):
        print("test_Darmangar_tedad_gheibat")
        self.assertEqual(self.darmangar.tedad_gheibat(self.clinic, "M001"),1)

if __name__ == "__main__":
    unittest.main()