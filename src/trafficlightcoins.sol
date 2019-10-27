pragma solidity >=0.4.22 <0.6.0;
import "remix_tests.sol"; // this import is automatically injected by Remix.

contract trafficlightcoins{
    
    
    mapping (string => uint) public trafficlights;
    
    function AddTrafficlight (string memory id) public {
        if(trafficlights[id]==0){
            trafficlights[id] = 0;

        }
    }
    
    function GetTrafficLightCoins (string memory id) public view returns(uint){
        return trafficlights[id];
    }
    
    function IncreaseTrafficLightCoins (string memory id, uint n) public {
        uint current_coins = trafficlights[id];
        current_coins= current_coins+n;
        trafficlights[id]=current_coins;
    }
}