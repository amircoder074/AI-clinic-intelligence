from src.Clinic_Analytics import Clinic, Darmangar, Moraje, Jalase

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