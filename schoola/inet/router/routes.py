from schoola.arch.mvc.helpers import MVCRoutingHelper
import schoola.modules.index.controllers as index_controllers
import schoola.modules.instructors.controllers as instructors_controllers
import schoola.modules.students.controllers as students_controllers
import schoola.modules.classrooms.controllers as classrooms_controllers
import schoola.modules.courses.controllers as courses_controllers
import schoola.modules.departments.controllers as departments_controllers
import schoola.modules.sections.controllers as sections_controllers
import schoola.modules.teaches.controllers as teaches_controllers
import schoola.modules.prerequirements.controllers as prerequirements_controllers
import schoola.modules.takes.controllers as takes_controllers
import schoola.modules.time_slots.controllers as time_slots_controllers

#  First element is routes list is stable. Means not generated dynamically.
#  The rest of them, come in convenient form for being added as url rule by server
#  from different controllers of models in modules.
#  And each url and name of themselves canalized to the arc > mvc > helpers > mvc routing helper function.
#  Its purpose is that adding actions ('create-read-update-delete-list) to each of them.
#  And appending the result of each function as items of this ROUTES list.
ROUTES = [
    {
        'name': 'index',
        'path': '/',
        'methods': ['GET'],
        'controller_class': index_controllers.IndexController,
    },
    *MVCRoutingHelper.build_crudl_routes(
        base_name='instructors',
        base_path='/instructors',
        controller_class=instructors_controllers.InstructorController,
    ),
    *MVCRoutingHelper.build_crudl_routes(
        base_name='students',
        base_path='/students',
        controller_class=students_controllers.StudentController,
    ),
    *MVCRoutingHelper.build_crudl_routes(
        base_name='classrooms',
        base_path='/classrooms',
        controller_class=classrooms_controllers.ClassroomController,
    ),
    *MVCRoutingHelper.build_crudl_routes(
        base_name='courses',
        base_path='/courses',
        controller_class=courses_controllers.CourseController,
    ),
    *MVCRoutingHelper.build_crudl_routes(
        base_name='departments',
        base_path='/departments',
        controller_class=departments_controllers.DepartmentController,
    ),
    *MVCRoutingHelper.build_crudl_routes(
        base_name='sections',
        base_path='/sections',
        controller_class=sections_controllers.SectionController,
    ),
    *MVCRoutingHelper.build_crudl_routes(
        base_name='teaches',
        base_path='/teaches',
        controller_class=teaches_controllers.TeachesController,
    ),
    *MVCRoutingHelper.build_crudl_routes(
        base_name='prerequirements',
        base_path='/prerequirements',
        controller_class=prerequirements_controllers.PrerequirementController,
    ),
    *MVCRoutingHelper.build_crudl_routes(
        base_name='takes',
        base_path='/takes',
        controller_class=takes_controllers.TakesController,
    ),
    *MVCRoutingHelper.build_crudl_routes(
        base_name='time_slots',
        base_path='/time_slots',
        controller_class=time_slots_controllers.TimeSlotController,
    )
]

ROUTES_BY_NAME = {}

for route in ROUTES:
    ROUTES_BY_NAME[route.get('name')] = route
