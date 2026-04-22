pragma solidity ^0.8.20;

contract Deals {

    struct Deal {
        address buyer;
        address seller;
        uint256 price;
        string item;
        uint256 timestamp;
    }

    Deal[] public deals;

    event DealCreated(
        uint256 indexed dealId,
        address indexed buyer,
        address indexed seller,
        uint256 price,
        string item,
        uint256 timestamp
    );

    function createDeal(
        address _buyer,
        address _seller,
        uint256 _price,
        string memory _item
    ) public {

        require(_buyer != address(0), "Invalid buyer");
        require(_seller != address(0), "Invalid seller");
        require(_price > 0, "Price must be > 0");

        Deal memory newDeal = Deal({
            buyer: _buyer,
            seller: _seller,
            price: _price,
            item: _item,
            timestamp: block.timestamp
        });

        deals.push(newDeal);

        emit DealCreated(
            deals.length - 1,
            _buyer,
            _seller,
            _price,
            _item,
            block.timestamp
        );
    }

    function getDealsCount() public view returns (uint256) {
        return deals.length;
    }

    function getDeal(uint256 _index) public view returns (
        address buyer,
        address seller,
        uint256 price,
        string memory item,
        uint256 timestamp
    ) {
        Deal memory d = deals[_index];
        return (d.buyer, d.seller, d.price, d.item, d.timestamp);
    }
}