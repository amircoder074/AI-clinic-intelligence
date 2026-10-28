import unittest
import Clinic_Analytics

class TestClinic_Analytics(unittest.TestCase) :

    def test_Moraje_sabt_moraje(self):
        clinic = Clinic_Analytics.Clinic("Khane Roshd")
        darmangar = Clinic_Analytics.Darmangar(clinic, "mamad", "ahmadi", "2110566450", 911512615, "kardarnmani", 5)
        moraje = Clinic_Analytics.Moraje(clinic, darmangar, "saeed", "mortazavi", "2121061185", 9122154789, "loknat","Hami")
        moraje.sabt_moraje()
        self.assertIn(moraje.code, clinic.morajein)
        self.assertEqual(clinic.morajein[moraje.code], "saeed mortazavi")


    def test_Moraje_tedad_jalasat_va_gheibat(self):
        clinic = Clinic_Analytics.Clinic("Clinic A")
        darmangar = Clinic_Analytics.Darmangar(clinic, "Dr. John", "Doe", "D001", 9121215689, "goftardarmani", 3)
        moraje = Clinic_Analytics.Moraje(clinic, darmangar, "Jane", "Smith", "M001", 1234567890, "None", "Hami")

        # Simulate adding sessions for the moraje
        clinic.jalasat[darmangar.code] = {
            moraje.code: [
                (1, 2, True, True),  # Attended session
                (3, 4, True, False),  # Missed session
                (5, 6, True, True)   # Attended session
            ]
        }

        self.assertEqual(moraje.tedad_jalasat(), 2)  # Should count only attended sessions
        self.assertEqual(moraje.tedad_gheibat(), 1)  # Should count only missed sessions

    def test_Moraje_hazineh_pardakhti(self):
        clinic = Clinic_Analytics.Clinic("Clinic B")
        darmangar = Clinic_Analytics.Darmangar(clinic, "Dr. Arabi", "Goe", "D002", 9157564789, "kardarmani", 4)
        moraje = Clinic_Analytics.Moraje(clinic, darmangar, "mania", "bardi", "M002", 1258793217, "Kalam", "Jame")

        j_1 = Clinic_Analytics.Jalase(clinic, darmangar, moraje,True,True)
        j_2 = Clinic_Analytics.Jalase(clinic, darmangar, moraje,True,True)
        j_3 = Clinic_Analytics.Jalase(clinic, darmangar, moraje,False,True)

        j_1.sabt_jalaseh()
        j_2.sabt_jalaseh()
        j_3.sabt_jalaseh()

        self.assertEqual(moraje.hazineh_pardakhti(clinic=clinic, darmangar=darmangar), 1000000)

    def test_Darmangar_tedad_gheibat(self):
        clinic = Clinic_Analytics.Clinic("Clinic C")
        darmangar = Clinic_Analytics.Darmangar(clinic, "Dr. Mahmudi", "Ade", "D003", 9144569874, "goftardarmani", 5)
        moraje = Clinic_Analytics.Moraje(clinic, darmangar, "sania", "musavi", "M003", 1258796412, "Falaje maghzi", "Jame vije")

        # Simulate adding sessions for the darmangar
        clinic.jalasat[darmangar.code] = {
            moraje.code: [
                (1, 2, True,True),  # Attended session
                (3, 4, False,True),  # Missed session
                (5, 6, False,True)   # Attended session
            ]
        }

        self.assertEqual(darmangar.tedad_gheibat(clinic=clinic, moraje_code="M003"),2)

if __name__ == "__main__":
    unittest.main()