// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from vision_msgs:msg/Point2D.idl
// generated code does not contain a copyright notice

#ifndef VISION_MSGS__MSG__DETAIL__POINT2_D__TRAITS_HPP_
#define VISION_MSGS__MSG__DETAIL__POINT2_D__TRAITS_HPP_

#include "vision_msgs/msg/detail/point2_d__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<vision_msgs::msg::Point2D>()
{
  return "vision_msgs::msg::Point2D";
}

template<>
inline const char * name<vision_msgs::msg::Point2D>()
{
  return "vision_msgs/msg/Point2D";
}

template<>
struct has_fixed_size<vision_msgs::msg::Point2D>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<vision_msgs::msg::Point2D>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<vision_msgs::msg::Point2D>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // VISION_MSGS__MSG__DETAIL__POINT2_D__TRAITS_HPP_
