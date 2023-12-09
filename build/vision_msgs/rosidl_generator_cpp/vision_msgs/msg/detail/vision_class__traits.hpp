// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from vision_msgs:msg/VisionClass.idl
// generated code does not contain a copyright notice

#ifndef VISION_MSGS__MSG__DETAIL__VISION_CLASS__TRAITS_HPP_
#define VISION_MSGS__MSG__DETAIL__VISION_CLASS__TRAITS_HPP_

#include "vision_msgs/msg/detail/vision_class__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<vision_msgs::msg::VisionClass>()
{
  return "vision_msgs::msg::VisionClass";
}

template<>
inline const char * name<vision_msgs::msg::VisionClass>()
{
  return "vision_msgs/msg/VisionClass";
}

template<>
struct has_fixed_size<vision_msgs::msg::VisionClass>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<vision_msgs::msg::VisionClass>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<vision_msgs::msg::VisionClass>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // VISION_MSGS__MSG__DETAIL__VISION_CLASS__TRAITS_HPP_
