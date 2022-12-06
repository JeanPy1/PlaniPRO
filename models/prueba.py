from db import Person, session

#persona = Person("48555618", "OROPEZA", "INCA", "JEANCARLOS ALBERTO", "01/01/2000", "10/10/2010", 1200, 102.50, 100,
#                "ONP", "MIXTA", "FDSDFSDFSDFD", "RRHH", "194578457845", "A48555618", "AI", "01/01/2030", "OFICINA",
#                 "984578457", "CHORRILLOS", "01/01/2020")
#session.add(persona)
#session.commit()

#print(persona)



result = session.query(Person).all()
#print(result)
for r in result:
    print(r)


#session.query(Person).filter(Person.id == 12).delete()
#session.commit()
#session.query(Person).filter(Person.id == 1).update({Person.dni: "00000000", Person.nombre: "AAAA"})
#session.commit()