// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from vision_msgs:msg/LabelInfo.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "vision_msgs/msg/detail/label_info__rosidl_typesupport_introspection_c.h"
#include "vision_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "vision_msgs/msg/detail/label_info__functions.h"
#include "vision_msgs/msg/detail/label_info__struct.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/header.h"
// Member `header`
#include "std_msgs/msg/detail/header__rosidl_typesupport_introspection_c.h"
// Member `class_map`
#include "vision_msgs/msg/vision_class.h"
// Member `class_map`
#include "vision_msgs/msg/detail/vision_class__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void LabelInfo__rosidl_typesupport_introspection_c__LabelInfo_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  vision_msgs__msg__LabelInfo__init(message_memory);
}

void LabelInfo__rosidl_typesupport_introspection_c__LabelInfo_fini_function(void * message_memory)
{
  vision_msgs__msg__LabelInfo__fini(message_memory);
}

size_t LabelInfo__rosidl_typesupport_introspection_c__size_function__VisionClass__class_map(
  const void * untyped_member)
{
  const vision_msgs__msg__VisionClass__Sequence * member =
    (const vision_msgs__msg__VisionClass__Sequence *)(untyped_member);
  return member->size;
}

const void * LabelInfo__rosidl_typesupport_introspection_c__get_const_function__VisionClass__class_map(
  const void * untyped_member, size_t index)
{
  const vision_msgs__msg__VisionClass__Sequence * member =
    (const vision_msgs__msg__VisionClass__Sequence *)(untyped_member);
  return &member->data[index];
}

void * LabelInfo__rosidl_typesupport_introspection_c__get_function__VisionClass__class_map(
  void * untyped_member, size_t index)
{
  vision_msgs__msg__VisionClass__Sequence * member =
    (vision_msgs__msg__VisionClass__Sequence *)(untyped_member);
  return &member->data[index];
}

bool LabelInfo__rosidl_typesupport_introspection_c__resize_function__VisionClass__class_map(
  void * untyped_member, size_t size)
{
  vision_msgs__msg__VisionClass__Sequence * member =
    (vision_msgs__msg__VisionClass__Sequence *)(untyped_member);
  vision_msgs__msg__VisionClass__Sequence__fini(member);
  return vision_msgs__msg__VisionClass__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember LabelInfo__rosidl_typesupport_introspection_c__LabelInfo_message_member_array[3] = {
  {
    "header",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(vision_msgs__msg__LabelInfo, header),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "class_map",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(vision_msgs__msg__LabelInfo, class_map),  // bytes offset in struct
    NULL,  // default value
    LabelInfo__rosidl_typesupport_introspection_c__size_function__VisionClass__class_map,  // size() function pointer
    LabelInfo__rosidl_typesupport_introspection_c__get_const_function__VisionClass__class_map,  // get_const(index) function pointer
    LabelInfo__rosidl_typesupport_introspection_c__get_function__VisionClass__class_map,  // get(index) function pointer
    LabelInfo__rosidl_typesupport_introspection_c__resize_function__VisionClass__class_map  // resize(index) function pointer
  },
  {
    "threshold",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(vision_msgs__msg__LabelInfo, threshold),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers LabelInfo__rosidl_typesupport_introspection_c__LabelInfo_message_members = {
  "vision_msgs__msg",  // message namespace
  "LabelInfo",  // message name
  3,  // number of fields
  sizeof(vision_msgs__msg__LabelInfo),
  LabelInfo__rosidl_typesupport_introspection_c__LabelInfo_message_member_array,  // message members
  LabelInfo__rosidl_typesupport_introspection_c__LabelInfo_init_function,  // function to initialize message memory (memory has to be allocated)
  LabelInfo__rosidl_typesupport_introspection_c__LabelInfo_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t LabelInfo__rosidl_typesupport_introspection_c__LabelInfo_message_type_support_handle = {
  0,
  &LabelInfo__rosidl_typesupport_introspection_c__LabelInfo_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_vision_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, vision_msgs, msg, LabelInfo)() {
  LabelInfo__rosidl_typesupport_introspection_c__LabelInfo_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  LabelInfo__rosidl_typesupport_introspection_c__LabelInfo_message_member_array[1].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, vision_msgs, msg, VisionClass)();
  if (!LabelInfo__rosidl_typesupport_introspection_c__LabelInfo_message_type_support_handle.typesupport_identifier) {
    LabelInfo__rosidl_typesupport_introspection_c__LabelInfo_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &LabelInfo__rosidl_typesupport_introspection_c__LabelInfo_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
