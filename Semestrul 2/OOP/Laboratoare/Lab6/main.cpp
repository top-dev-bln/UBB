#include "ui.h"
#include "tests.h"
#include "service.h"

int main() {
    testall();
    Repository repo;
    Validator validator(repo);
    Service servic(repo, validator);
    UI ui(servic);
    ui.run();
    return 0;
}