from dataclasses import dataclass, field
from typing import ClassVar
import datetime
import logging

logger = logging.getLogger('__name__')
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('sample.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

@dataclass
class Clinic:
    name : str
    darmangaran :  dict = field(default_factory=dict)
    morajein : dict = field(default_factory=dict)
    jalasat : dict = field(default_factory=dict)
    all_clinics : ClassVar[list["Clinic"]] = []

    def __post_init__(self):
        self.all_clinics.append(self)

@dataclass
class Darmangar:
    clinic : Clinic
    first_name : str
    last_name : str
    code : str 
    shomare_tamas : float
    takhasos : str
    sabeghe : float
    
    def sabt_darmangar(self):
        if self.code not in self.clinic.darmangaran.keys() : 
            self.clinic.darmangaran[self.code] = self.first_name + " " + self.last_name
        else : 
            print('{} dar list darmangaran hast..!'.format(self.first_name, self.last_name))
        logger.info('Afzoudan Darmangar : {} {} - {} - {}'.format(self.first_name, self.last_name, self.code, self.clinic.name))


    def hazf_darmangar(self):
        if self.code in self.clinic.darmangaran.keys() : 
            del self.clinic.darmangaran[self.code]
        else : 
            print('{} dar list darmangaran nist..!'.format(self.first_name, self.last_name))
        logger.info('Hazf Darmangar : {} {} - {} - {}'.format(self.first_name, self.last_name, self.code, self.clinic.name))
    
    def tedad_gheibat(self, clinic: Clinic | None = None, moraje_code :str = None) -> int:
        clinics = [clinic] if clinic is not None else Clinic.all_clinics

        return sum(
            not session[2]
            for current_clinic in clinics
            for darmangar_code, morajein in current_clinic.jalasat.items()
            if darmangar_code == self.code
            for morajecode, sessions in morajein.items()
            if moraje_code is None or morajecode == moraje_code
            for session in sessions)

    @property
    def moshakhasat_darmangar(self):
        return '{} {} - {} - {}'.format(self.first_name, self.last_name, self.takhasos, self.sabeghe)

    @staticmethod
    def barresi_code(code : str):
        if len(code) != 10 or not code.isdigit():
            raise ValueError("Code bayad yek adad 10 raghami bashad.")
        if len(set(code)) == 1: 
            raise ValueError("Code nabayad daraye adad yeksan bashad.")
        total = sum(int(digit) * (10 - index) for index, digit in enumerate(code[:-1]))
        reminder = total % 11

        check_digit = int(code[-1])
        try : 
            if (reminder < 2 and check_digit == reminder) or (reminder >= 2 and check_digit == 11 - reminder):
                raise Exception
        except Exception : 
            print("Code vared shode motabar hast..:)")
        else : 
            return True

    @classmethod 
    def set_zarayeb_rotbebandi(cls, a1: float, a2: float, b1: float, c1: float, c2: float) :
        cls.a1 = a1
        cls.a2 = a2
        cls.b1 = b1
        cls.c1 = c1
        cls.c2 = c2

@dataclass
class Moraje:
    clinic : Clinic
    darmangar : Darmangar
    first_name : str
    last_name : str
    code : str
    shomare_tamas : float
    ekhtelal : str
    noe_tarh : str

    def sabt_moraje(self):
        if self.code not in self.clinic.morajein.keys() : 
            self.clinic.morajein[self.code] = self.first_name + " " + self.last_name
        else : 
            print('{} dar list morajein hast..!'.format(self.first_name, self.last_name))
        logger.info('Afzoudan Moraje : {} {} {} - {} - {} {}'.format(self.first_name, self.last_name, self.code, self.clinic.name, self.darmangar.first_name, self.darmangar.last_name))

    def tedad_jalasat(self, clinic: Clinic | None = None, darmangar: Darmangar | None = None) -> int:
        clinics = [clinic] if clinic is not None else Clinic.all_clinics

        return sum(
            session[2] and session[3]
            for current_clinic in clinics
            for darmangar_code, morajein in current_clinic.jalasat.items()
            if darmangar is None or darmangar_code == darmangar.code
            for session in morajein.get(self.code, []))
    
    def tedad_gheibat(self, clinic: Clinic | None = None, darmangar: Darmangar | None = None) -> int:
        clinics = [clinic] if clinic is not None else Clinic.all_clinics

        return sum(
            not session[3]
            for current_clinic in clinics
            for darmangar_code, morajein in current_clinic.jalasat.items()
            if darmangar is None or darmangar_code == darmangar.code
            for session in morajein.get(self.code, []))
    
    def hazineh_pardakhti(self,clinic: Clinic | None = None, darmangar: Darmangar | None = None) -> int:
        nerkh = {
            "Hami": 250000,
            "Payeh": 300000,
            "Jame": 500000,
            "Jame vije": 900000,
        }
        return self.tedad_jalasat(clinic, darmangar) * nerkh[self.noe_tarh]

    @property 
    def vaziat(self):
        return 'Vaziat Moraje is - {}'.format(self._vaziat)

    @vaziat.setter
    def vaziat(self, name : str):
        self._vaziat = name

    @vaziat.deleter
    def vaziat(self):
        print("Deleted Vaziat!")
        self._vaziat = None

@dataclass 
class Jalase: 
    clinic : Clinic
    darmangar : Darmangar
    moraje : Moraje
    vaziat_darmangar : bool = True
    vaziat_moraje : bool = True
    tarikh : datetime = field(default_factory=datetime.datetime.now)

    def sabt_jalaseh(self):
        self.clinic.jalasat.setdefault(self.darmangar.code, {}).setdefault(self.moraje.code, [])
        index = len(self.clinic.jalasat[self.darmangar.code][self.moraje.code]) + 1
        self.clinic.jalasat[self.darmangar.code][self.moraje.code].append([index, self.tarikh, self.vaziat_darmangar, self.vaziat_moraje])
        logger.info('Jalase Bargozar Shodeh : {} - {} {} - {} {} - {} {}'.format(self.clinic.name, self.darmangar.first_name, self.darmangar.last_name, self.moraje.first_name, self.moraje.last_name, self.vaziat_darmangar, self.vaziat_moraje))


def main():
    cl_1 = Clinic("Khane Roshd")
    dr_1 = Darmangar(cl_1, "mamad", "ahmadi", "2110566450", 911512615, "kardarnmani", 5)
    dr_2 = Darmangar(cl_1, "mahdi", "ahmadi", "2110236728", 915512615, "goftardarmani", 3)
    dr_1.sabt_darmangar()
    dr_2.sabt_darmangar()
    mr_1 = Moraje(cl_1, dr_1, "saeed", "mortazavi", "2121061185", 9122154789, "loknat","Hami")
    mr_2 = Moraje(cl_1, dr_1, "javid", "mortazavi", "2110566789", 9132154789, "loknat","Jame")
    mr_1.sabt_moraje()
    mr_2.sabt_moraje()
    j_1 = Jalase(cl_1, dr_1, mr_1,True,False)
    j_2 = Jalase(cl_1, dr_1, mr_1,False,True)
    j_3 = Jalase(cl_1, dr_1, mr_1,False,True)
    j_4 = Jalase(cl_1, dr_1, mr_1,True,True)
    j_5 = Jalase(cl_1, dr_2, mr_1,True,True)
    j_1.sabt_jalaseh()
    j_2.sabt_jalaseh()
    j_3.sabt_jalaseh()
    j_4.sabt_jalaseh()
    j_5.sabt_jalaseh()
    mr_1.vaziat = 'Erjaei'
    print(mr_1.vaziat)
    print(cl_1.jalasat)
    print(dr_1.tedad_gheibat())


if __name__ == "__main__":
    main()
