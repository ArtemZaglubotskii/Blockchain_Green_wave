pragma solidity >=0.4.22 <0.6.0;
import "remix_tests.sol"; // this import is automatically injected by Remix.

contract carscoins{
    
    struct NumberCoins {
        string number;
        uint coins;
    }
    
    address owner = 0xCA35b7d915458EF540aDe6068dFe2F44E8fa733c;
    
    mapping (string => NumberCoins) public cars;
    mapping (string => string) public uinum;
    
    function AddCar (string memory ui, string memory number) public {
        if(msg.sender==owner){
            if(!isNumberExist(number)){
                cars[ui].number = number;
                cars[ui].coins = 0;
                uinum[number] = ui;
            }
        }
    }
    
    function GetUIFromNumber (string memory number) public view returns (string memory){
        if(msg.sender==owner){
            return uinum[number];
        }
    }
    
    function isNumberExist (string memory number) public view returns(bool){
        if(!compareStrings(uinum[number], "")){
            return true;
        }
    }

    function GetCarCoinsFromUI (string memory ui) public view returns (uint){
        if(msg.sender==owner){
            return cars[ui].coins;
        }
    }
    
    function GetCarNumberFromUI (string memory ui) public view returns (string memory){
        if(msg.sender==owner){
            return cars[ui].number;
        }
    }
    
     function AddCoinByUI (string memory ui) public {
         if(msg.sender==owner){
             uint current_coins = cars[ui].coins;
             current_coins = current_coins+1;
             cars[ui].coins=current_coins;
         }
    }
    
    
    
    function compareStrings (string memory a, string memory b) public view returns (bool) {
        return (keccak256(abi.encodePacked((a))) == keccak256(abi.encodePacked((b))) );
    }
    
}