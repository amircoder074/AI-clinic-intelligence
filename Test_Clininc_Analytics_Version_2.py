from Clinic_Analytics import Clinic, Darmangar, Moraje, Jalase
import pytest

class TestClinic_Analytics:

    @pytest.fixture(scope='function', autouse=True)
    def ClinicAnalitic(self): 
        print("Settingup operation\n")
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

        yield self.clinic, self.darmangar, self.moraje  
        self.clinic.darmangaran.clear()
        self.clinic.morajein.clear()
        self.clinic.jalasat.clear()
        print("Tearingdown operation\n")


    def test_Moraje_sabt_moraje(self):
        print("test_Moraje_sabt_moraje")
        assert self.moraje.code in self.clinic.morajein
        assert self.clinic.morajein[self.moraje.code] ==  "Goe Antimuli"

    @pytest.mark.slow
    def test_Moraje_tedad_jalasat_va_gheibat(self):
        print("test_Moraje_tedad_jalasat_va_gheibat")
        assert self.moraje.tedad_jalasat() == 1
        assert self.moraje.tedad_gheibat() == 1

    def test_Moraje_hazineh_pardakhti(self):
        print("test_Moraje_hazineh_pardakhti")
        assert self.moraje.hazineh_pardakhti(self.clinic, self.darmangar) == 900000

    def test_Darmangar_tedad_gheibat(self):
        print("test_Darmangar_tedad_gheibat")
        assert self.darmangar.tedad_gheibat(self.clinic, "M001") == 1