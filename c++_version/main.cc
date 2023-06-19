#include <SFML/Graphics.hpp>
#include "logic.cc"

int WINDOW_SIZE = 1000;
int ROWS = 250;

using namespace std;

typedef vector< vector< int>> Matrix;

int main()
{

    sf::RenderWindow window(sf::VideoMode(WINDOW_SIZE, WINDOW_SIZE), "Backyard Mob");
    sf::VertexArray lines(sf::LinesStrip, 2);
    sf::RectangleShape cell(sf::Vector2f(int(WINDOW_SIZE/ROWS), int(WINDOW_SIZE/ROWS)));


    bool selection_screen = true;
    
    Matrix matrix = generate_random(ROWS);

    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();

            else if (event.type == sf::Event::MouseButtonPressed) {
                if (event.mouseButton.button == sf::Mouse::Right and selection_screen) matrix = generate_random(ROWS);
            }

            else if (event.type == sf::Event::KeyPressed) {
                if (event.key.code == sf::Keyboard::Space) {
                    selection_screen = false;
                }
            }
        }

        window.clear();
       
        // Drawing Cells

        if (selection_screen) {

            for (int i = 0; i < ROWS; ++i) {
                for (int j = 0; j < ROWS; ++j) {
                    cell.setPosition(sf::Vector2f(i*(WINDOW_SIZE/ROWS), j*(WINDOW_SIZE/ROWS)));
                    if (matrix[i][j] == 1) {
                        cell.setFillColor(sf::Color::Green);
                    } else if (matrix[i][j] == 2) {
                        cell.setFillColor(sf::Color::Red);
                    } else {
                        if (count_around(matrix, i, j).first > count_around(matrix, i, j).second) cell.setFillColor(sf::Color::Green);
                        else cell.setFillColor(sf::Color::Red);
                    }
                    window.draw(cell);
                }
            } 
        
            window.display();
        }

        else {
            for (int i = 0; i < ROWS; ++i) {
                for (int j = 0; j < ROWS; ++j) {
                    cell.setPosition(sf::Vector2f(i*(WINDOW_SIZE/ROWS), j*(WINDOW_SIZE/ROWS)));
                    if (matrix[i][j] == 1) {
                        cell.setFillColor(sf::Color::Green);
                    } else if (matrix[i][j] == 2) {
                        cell.setFillColor(sf::Color::Red);
                    } else {
                        if (count_around(matrix, i, j).first > count_around(matrix, i, j).second) cell.setFillColor(sf::Color::Green);
                        else cell.setFillColor(sf::Color::Red);
                    }
                    window.draw(cell);
                }
            } 
        
            window.display();

            update_cells(matrix);

        }
    }

    return 0;
}