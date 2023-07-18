#include <iostream>
#include <chrono>
#include "behaviortree_cpp/action_node.h"
#include "behaviortree_cpp/bt_factory.h"

using namespace std::chrono_literals;

/**
 * Toggle Controls
*/

class ToggleControls : public BT::SyncActionNode
{
    public:
        // Constructor
        explicit ToggleControls(const std::string &name) : BT::SyncActionNode(name, {})
        {
        }

        BT::NodeStatus tick() override
        {
            std::this_thread::sleep_for(3s);
            std::cout << "Toggled Controls" << std::endl;
            return BT::NodeStatus::SUCCESS;
        }
};


/**
 * Reset Pose
*/

class ResetPose : public BT::SyncActionNode
{
    public:
        // Constructor
        explicit ResetPose(const std::string &name) : BT::SyncActionNode(name, {})
        {
        }

        BT::NodeStatus tick() override
        {
            std::this_thread::sleep_for(3s);
            std::cout << "Pose Reset" << std::endl;
            return BT::NodeStatus::SUCCESS;
        }
};


/**
 * GoTo
*/

class GoTo : public BT::SyncActionNode
{
    public:
        // Constructor
        explicit GoTo(const std::string &name, const BT::NodeConfig &config) 
            : BT::SyncActionNode(name, config)
        {
        }

        static BT::PortsList providedPorts()
        {
            return {BT::InputPort<std::vector<int>>("location")};
        }

        BT::NodeStatus tick() override
        {
            auto msg = getInput<std::vector<int>>("location");
            std::this_thread::sleep_for(3s);
            std::cout << "Going to x, y" << std::endl;
            return BT::NodeStatus::SUCCESS;
        }
};


/**
 * GetDetectedObjects
*/

class GetDetectedObjects : public BT::SyncActionNode
{
    public:
        // Constructor
        explicit GetDetectedObjects(const std::string &name) : BT::SyncActionNode(name, {})
        {
        }

        static BT::PortsList providedPorts()
        {
            return {BT::OutputPort<std::vector<int>>("object_location")};
        }

        BT::NodeStatus tick() override
        {
            std::this_thread::sleep_for(3s);
            std::vector<int> objectLocation{1, 2, 3};
            BT::TreeNode::setOutput("object_location", objectLocation);
            std::cout << "Got the detected objects" << std::endl;
            return BT::NodeStatus::SUCCESS;
        }
};

/**
 * GetGate
*/

class GetGate : public BT::SyncActionNode
{
    public:
        // Constructor
        explicit GetGate(const std::string &name) : BT::SyncActionNode(name, {})
        {
        }

        BT::NodeStatus tick() override
        {
            std::this_thread::sleep_for(3s);
            std::vector<int> gateLocation{2, 4, 6};
            BT::TreeNode::setOutput("object_location", gateLocation);
            std::cout << "Got the gate" << std::endl;
            return BT::NodeStatus::SUCCESS;
        }
};


/**
 * IsGateCentered
*/

BT::NodeStatus isGateCentered(BT::TreeNode &self)
{
    auto msg = self.getInput<std::vector<int>>("gate_location");

    if(!msg)
    {
        throw BT::RuntimeError("missing require input[message]: ", msg.error());
    }

    for (const auto position_coordinate : msg.value())
    {
        std::cout << position_coordinate << ' ';
    }

    std::cout << "Gate is centered" << std::endl;
    return BT::NodeStatus::SUCCESS;
};

int main()
{
    BT::BehaviorTreeFactory factory;

    // Register Nodes
    factory.registerNodeType<ToggleControls>("ToggleControls");
    factory.registerNodeType<ResetPose>("ResetPose");
    factory.registerNodeType<GoTo>("GoTo");
    factory.registerNodeType<GetDetectedObjects>("GetDetectedObjects");
    factory.registerNodeType<GetGate>("GetGate");
    factory.registerSimpleCondition("IsGateCentered", std::bind(isGateCentered));

    // Create Tree
    auto tree = factory.createTreeFromFile("./../tasks_tree.xml");

    // Execute the Tree
    tree.tickWhileRunning();

    return 0;
}