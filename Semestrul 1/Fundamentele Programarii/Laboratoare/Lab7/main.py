from ui.console import Consola

from domain.validator_student import ValidatorStudent
from domain.validator_laborator import ValidatorLaborator

from repository.repo_studenti import RepoStudenti
from repository.repo_laborator import RepoLaborator

from service.service_studenti import ServiceStudenti
from service.service_laborator import ServiceLaborator


from tests.teste import Teste
Test = Teste()
Test.ruleaza_toate_testele()
validator_student = ValidatorStudent()
repo_studenti = RepoStudenti()


validator_laborator = ValidatorLaborator()
repo_laborator = RepoLaborator()
service_laboratoare = ServiceLaborator(validator_laborator,repo_laborator)
service_studenti = ServiceStudenti(validator_student, repo_studenti, service_laboratoare)
consola = Consola(service_studenti, service_laboratoare)

consola.run()