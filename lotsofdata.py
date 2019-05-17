#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Admin, Base, Downloads, Departments, Facaulties, Students

# Connect to Database and create database session
engine = create_engine('sqlite:///collegedemo.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create dummy data
Admin1 = Admin(name="Amit Kumar",
               email="ak125846@gmail.com",
               password="123456",
               picture='https://bit.ly/2NOadS1')
session.add(Admin1)
session.commit()


downloads1 = Downloads(file_name="Fee Structure B.Tech '19",
                       file_path="/static/FEE_STRUCTURE_ENGG.pdf",
                       admin_id="1")
session.add(downloads1)
session.commit()


downloads2 = Downloads(file_name="Fee Structure MCA'19",
                       file_path="/static/FEE_STRUCTURE_MCA.pdf",
                       admin_id="1")
session.add(downloads2)
session.commit()


downloads3 = Downloads(file_name="Fee Structure M.Tech '19",
                       file_path="/static/FEE_STRUCTURE_MTECH.pdf",
                       admin_id="1")
session.add(downloads3)
session.commit()


downloads4 = Downloads(file_name="Affidavit Anti Ragging - Student",
                       file_path="/static/affidavit_Student_ragging.pdf",
                       admin_id="1")
session.add(downloads4)
session.commit()


downloads5 = Downloads(file_name="Affidavit Anti Ragging - Guardian",
                       file_path="/static/affidavit_Guardian_ragging.pdf",
                       admin_id="1")
session.add(downloads5)
session.commit()


departments1 = Departments(dept_name="Computer Science & Engineering",
                           srt_name="CSE")
session.add(departments1)
session.commit()


departments2 = Departments(dept_name="ELECTRONICS & COMMUNICATION ENGINEERING",
                           srt_name="ESE")
session.add(departments2)
session.commit()


departments3 = Departments(dept_name="BASIC SCIENCES & HUMANITIES",
                           srt_name="HU")
session.add(departments3)
session.commit()

departments4 = Departments(dept_name="APPLIED ELECTRONICS & INSTRUMENTATION ENGINEERING",
                           srt_name="AEIE")
session.add(departments4)
session.commit()

departments5 = Departments(dept_name="ELECTRICAL ENGINEERING",
                           srt_name="EE")
session.add(departments5)
session.commit()

departments6 = Departments(dept_name="MECHANICAL ENGINEERING",
                           srt_name="ME")
session.add(departments6)
session.commit()


departments7 = Departments(dept_name="CIVIL ENGINEERING",
                           srt_name="CE")
session.add(departments7)
session.commit()


facaulty1 = Facaulties(fac_name="Dr. Sanjay Biswas",
                       picture="",
                       email="ak1@gmail.com",
                       password="123456",
                       ac_rank="Professor",
                       edu="",
                       dept_id="1",
                       admin_id="1")
session.add(facaulty1)
session.commit()


facaulty2 = Facaulties(fac_name="Dr. Dipendra Nath Ghosh",
                       picture="",
                       email="ak2@gmail.com",
                       password="123456",
                       ac_rank="Professor",
                       edu="",
                       dept_id="1",
                       admin_id="1")
session.add(facaulty2)
session.commit()

facaulty3 = Facaulties(fac_name="Dr. Chandan Konar",
                       picture="/static/c_conar.png",
                       email="ak3@gmail.com",
                       password="123456",
                       ac_rank="Head of the Department",
                       edu="B.Tech, M.Tech, Ph.D",
                       dept_id="1",
                       admin_id="1")
session.add(facaulty3)
session.commit()


facaulty4 = Facaulties(fac_name="Biswadeb Goswami",
                       picture="",
                       email="ak4@gmail.com",
                       password="123456",
                       ac_rank="Professor",
                       edu="",
                       dept_id="1",
                       admin_id="1")
session.add(facaulty4)
session.commit()


facaulty5 = Facaulties(fac_name="Dr. Subir Halder",
                       picture="",
                       email="ak5@gmail.com",
                       password="123456",
                       ac_rank="Professor",
                       edu="",
                       dept_id="1",
                       admin_id="1")
session.add(facaulty5)
session.commit()


facaulty6 = Facaulties(fac_name="Dr. Raj Kumar Samanta",
                       picture="/static/HOD-IT.jpg",
                       email="ak6@gmail.com",
                       password="123456",
                       ac_rank="Head of the Department",
                       edu="B.Tech.(NIT Hamirpur), M.Tech.(NIT, Bhopal), PhD (NIT, Dgp)",
                       dept_id="2",
                       admin_id="1")
session.add(facaulty6)
session.commit()


facaulty7 = Facaulties(fac_name="Dinesh Kumar Pradhan",
                       picture="",
                       email="ak7@gmail.com",
                       password="123456",
                       ac_rank="Professor",
                       edu="",
                       dept_id="2",
                       admin_id="1")
session.add(facaulty7)
session.commit()


facaulty8 = Facaulties(fac_name="Saikat Maity",
                       picture="",
                       email="ak8@gmail.com",
                       password="123456",
                       ac_rank="Professor",
                       edu="",
                       dept_id="2",
                       admin_id="1")
session.add(facaulty8)
session.commit()


facaulty9 = Facaulties(fac_name="Prabal Kumar Sahu",
                       picture="",
                       email="ak9@gmail.com",
                       password="123456",
                       ac_rank="Professor",
                       edu="",
                       dept_id="2",
                       admin_id="1")
session.add(facaulty9)
session.commit()


facaulty10 = Facaulties(fac_name="Avijit Bhowmick",
                       picture="",
                       email="ak11@gmail.com",
                       password="123456",
                       ac_rank="Professor",
                       edu="",
                       dept_id="2",
                       admin_id="1")
session.add(facaulty10)
session.commit()


facaulty11 = Facaulties(fac_name="Dr. Sabyasachi Chandra",
                       picture="/static/HOD-CE.jpg",
                       email="ak12@gmail.com",
                       password="123456",
                       ac_rank="Head of the Department",
                       edu="B.E (Civil), M.Tech (Structural Engg, IITG), Ph.D. (Struct. Engg, IITKgp)",
                       dept_id="3",
                       admin_id="1")
session.add(facaulty11)
session.commit()


facaulty12 = Facaulties(fac_name="Subhransu Goswami",
                       picture="",
                       email="ak13@gmail.com",
                       password="123456",
                       ac_rank="Professor",
                       edu="",
                       dept_id="3",
                       admin_id="1")
session.add(facaulty12)
session.commit()


facaulty13 = Facaulties(fac_name="Koushik Mondal",
                       picture="",
                       email="ak14@gmail.com",
                       password="123456",
                       ac_rank="Professor",
                       edu="",
                       dept_id="3",
                       admin_id="1")
session.add(facaulty13)
session.commit()


facaulty14 = Facaulties(fac_name="Dr. Kanchan Chatterjee",
                       picture="/static/Hod-me.jpg",
                       email="ak15@gmail.com",
                       password="123456",
                       ac_rank="Head of the Department ",
                       edu="BE, M.E., Ph.D",
                       dept_id="4",
                       admin_id="1")
session.add(facaulty14)
session.commit()


facaulty14 = Facaulties(fac_name="Dr. Chandan Chattoraj",
                       picture="",
                       email="ak16@gmail.com",
                       password="123456",
                       ac_rank="Professor",
                       edu="",
                       dept_id="4",
                       admin_id="1")
session.add(facaulty14)
session.commit()


facaulty15 = Facaulties(fac_name="Dr. Swapan Kumar Majumder",
                       picture="",
                       email="ak17@gmail.com",
                       password="123456",
                       ac_rank="Professor",
                       edu="",
                       dept_id="4",
                       admin_id="1")
session.add(facaulty15)
session.commit()

facaulty16 = Facaulties(fac_name="Dr. Narendranath Pathak",
                       picture="/static/hod-ece.png",
                       email="ak18@gmail.com",
                       password="123456",
                       ac_rank="Head of the Department",
                       edu="BE, M.Tech, Ph.D ",
                       dept_id="5",
                       admin_id="1")
session.add(facaulty16)
session.commit()


facaulty17 = Facaulties(fac_name="Anirban Bose",
                       picture="",
                       email="ak19@gmail.com",
                       password="123456",
                       ac_rank="Professor",
                       edu="",
                       dept_id="5",
                       admin_id="1")
session.add(facaulty17)
session.commit()

facaulty18 = Facaulties(fac_name="Indranil Sengupta",
                       picture="",
                       email="ak21@gmail.com",
                       password="123456",
                       ac_rank="Professor",
                       edu="",
                       dept_id="5",
                       admin_id="1")
session.add(facaulty18)
session.commit()


facaulty19 = Facaulties(fac_name="Dr. Sumit Banerjee",
                       picture="/static/hod-ee.png",
                       email="ak22@gmail.com",
                       password="123456",
                       ac_rank="Head of the Department",
                       edu="B.E(Hons), ME, Ph.D",
                       dept_id="6",
                       admin_id="1")
session.add(facaulty19)
session.commit()


facaulty20 = Facaulties(fac_name="Dr. Susanta Dutta",
                       picture="",
                       email="ak23@gmail.com",
                       password="123456",
                       ac_rank="Professor",
                       edu="",
                       dept_id="6",
                       admin_id="1")
session.add(facaulty20)
session.commit()


facaulty21 = Facaulties(fac_name="Dr. Khondekar Mofazzal Hossain",
                       picture="/static/hod-aeie.png",
                       email="ak24@gmail.com",
                       password="123456",
                       ac_rank="Head of the Department",
                       edu="B.Sc.(JU), B.Tech.(JU), M.Tech.(NIT, Dgp), PhD (NIT, Dgp)",
                       dept_id="6",
                       admin_id="7")
session.add(facaulty21)
session.commit()


facaulty22 = Facaulties(fac_name="Sujit Kumar Chatterjee",
                       picture="",
                       email="ak25@gmail.com",
                       password="123456",
                       ac_rank="Professor",
                       edu="",
                       dept_id="7",
                       admin_id="1")
session.add(facaulty22)
session.commit()

student1 = Students(st_name="Amit Kumar",
                       picture="",
                       roll_no="12000115017",
                       mob_no = "9852972838",
                       dept_id="1",
                       admin_id="1")
session.add(student1)
session.commit()


print("added data!")
