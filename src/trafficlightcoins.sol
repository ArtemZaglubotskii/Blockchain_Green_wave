pragma solidity >=0.4.22 <0.6.0;
import "remix_tests.sol"; // this import is automatically injected by Remix.

contract trafficlightcoins{
    
    address owner = 0xC9f2894007155520CcB8591b3Ce833fF89754b73;
    
    mapping (string => uint) public trafficlights;
    
    function AddTrafficlight (string memory id) public {
        if(msg.sender==owner){
            if(trafficlights[id]==0){
                trafficlights[id] = 0;

            }
        }
    }
    
    function GetTrafficLightCoins (string memory id) public view returns(uint){
        if(msg.sender==owner){
            return trafficlights[id];
        }
    }
    
    function IncreaseTrafficLightCoins (string memory id, uint n) public {
        if(msg.sender==owner){
            uint current_coins = trafficlights[id];
            current_coins= current_coins+n;
            trafficlights[id]=current_coins;
        }
    }
}