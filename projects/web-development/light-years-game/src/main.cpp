#include "core/Application.h"

int main()
{
    ly::Application app{ 1024, 768, "Light Years" };
    app.Run();
    return 0;
}
