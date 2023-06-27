import game.sound.echo #py파일까지 들어가야한다.
#__init__파일이 없다면 패키지로 인식되지 않는다.
game.sound.echo.echo_test()
from game.sound import echo
echo.echo_test()
from game.sound.echo import echo_test
echo_test()

