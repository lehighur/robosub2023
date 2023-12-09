// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from vision_msgs:msg/VisionClass.idl
// generated code does not contain a copyright notice

#ifndef VISION_MSGS__MSG__DETAIL__VISION_CLASS__STRUCT_H_
#define VISION_MSGS__MSG__DETAIL__VISION_CLASS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'class_name'
#include "rosidl_runtime_c/string.h"

// Struct defined in msg/VisionClass in the package vision_msgs.
typedef struct vision_msgs__msg__VisionClass
{
  uint16_t class_id;
  rosidl_runtime_c__String class_name;
} vision_msgs__msg__VisionClass;

// Struct for a sequence of vision_msgs__msg__VisionClass.
typedef struct vision_msgs__msg__VisionClass__Sequence
{
  vision_msgs__msg__VisionClass * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} vision_msgs__msg__VisionClass__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // VISION_MSGS__MSG__DETAIL__VISION_CLASS__STRUCT_H_
