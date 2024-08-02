from models.employee import Employee
from models.base import SessionLocal


def get_employees():
    session = SessionLocal()
    result_set = session.query(Employee).all()
    return [employee.to_dict() for employee in result_set]


def create_employee(name, position):
    try:
        session = SessionLocal()
        employee = Employee(name=name, position=position)
        session.add(employee)
        session.commit()
    except Exception as ex:
        raise ex


def delete_employee(_id):
    pass


def update_employee(**kwargs):
    pass





