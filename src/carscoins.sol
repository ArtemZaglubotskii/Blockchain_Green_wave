pragma solidity >=0.4.22 <0.6.0;
import "remix_tests.sol"; // this import is automatically injected by Remix.

contract carscoins{
    
    address owner = 0xC9f2894007155520CcB8591b3Ce833fF89754b73;
    
    mapping (string => uint) public cars;
    
    function AddCar (string memory number) public {
        if(msg.sender==owner){
            if(cars[number]==0){
                cars[number]=0;
            }
        }
    }
    
    function AddCoinByNumber (string memory number, uint n) public {
        if(msg.sender==owner){
            uint current_coins = cars[number];
            current_coins = current_coins+n;
            cars[number]=current_coins;
        }
    }
    
    function GetCoinByNumber (string memory number) public view returns(uint){
        if(msg.sender==owner){
            return cars[number];
        }
    }

}