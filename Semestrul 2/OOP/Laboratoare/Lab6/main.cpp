#include "ui.h"
#include "tests.h"
#include "service.h"


int main() {
    testall();
    Service servic;
    UI ui(servic);
    ui.run();
    return 0;
}