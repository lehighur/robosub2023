// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from vision_msgs:msg/LabelInfo.idl
// generated code does not contain a copyright notice
#include "vision_msgs/msg/detail/label_info__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"
// Member `class_map`
#include "vision_msgs/msg/detail/vision_class__functions.h"

bool
vision_msgs__msg__LabelInfo__init(vision_msgs__msg__LabelInfo * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    vision_msgs__msg__LabelInfo__fini(msg);
    return false;
  }
  // class_map
  if (!vision_msgs__msg__VisionClass__Sequence__init(&msg->class_map, 0)) {
    vision_msgs__msg__LabelInfo__fini(msg);
    return false;
  }
  // threshold
  return true;
}

void
vision_msgs__msg__LabelInfo__fini(vision_msgs__msg__LabelInfo * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // class_map
  vision_msgs__msg__VisionClass__Sequence__fini(&msg->class_map);
  // threshold
}

bool
vision_msgs__msg__LabelInfo__are_equal(const vision_msgs__msg__LabelInfo * lhs, const vision_msgs__msg__LabelInfo * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__are_equal(
      &(lhs->header), &(rhs->header)))
  {
    return false;
  }
  // class_map
  if (!vision_msgs__msg__VisionClass__Sequence__are_equal(
      &(lhs->class_map), &(rhs->class_map)))
  {
    return false;
  }
  // threshold
  if (lhs->threshold != rhs->threshold) {
    return false;
  }
  return true;
}

bool
vision_msgs__msg__LabelInfo__copy(
  const vision_msgs__msg__LabelInfo * input,
  vision_msgs__msg__LabelInfo * output)
{
  if (!input || !output) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__copy(
      &(input->header), &(output->header)))
  {
    return false;
  }
  // class_map
  if (!vision_msgs__msg__VisionClass__Sequence__copy(
      &(input->class_map), &(output->class_map)))
  {
    return false;
  }
  // threshold
  output->threshold = input->threshold;
  return true;
}

vision_msgs__msg__LabelInfo *
vision_msgs__msg__LabelInfo__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  vision_msgs__msg__LabelInfo * msg = (vision_msgs__msg__LabelInfo *)allocator.allocate(sizeof(vision_msgs__msg__LabelInfo), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(vision_msgs__msg__LabelInfo));
  bool success = vision_msgs__msg__LabelInfo__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
vision_msgs__msg__LabelInfo__destroy(vision_msgs__msg__LabelInfo * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    vision_msgs__msg__LabelInfo__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
vision_msgs__msg__LabelInfo__Sequence__init(vision_msgs__msg__LabelInfo__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  vision_msgs__msg__LabelInfo * data = NULL;

  if (size) {
    data = (vision_msgs__msg__LabelInfo *)allocator.zero_allocate(size, sizeof(vision_msgs__msg__LabelInfo), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = vision_msgs__msg__LabelInfo__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        vision_msgs__msg__LabelInfo__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
vision_msgs__msg__LabelInfo__Sequence__fini(vision_msgs__msg__LabelInfo__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      vision_msgs__msg__LabelInfo__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

vision_msgs__msg__LabelInfo__Sequence *
vision_msgs__msg__LabelInfo__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  vision_msgs__msg__LabelInfo__Sequence * array = (vision_msgs__msg__LabelInfo__Sequence *)allocator.allocate(sizeof(vision_msgs__msg__LabelInfo__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = vision_msgs__msg__LabelInfo__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
vision_msgs__msg__LabelInfo__Sequence__destroy(vision_msgs__msg__LabelInfo__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    vision_msgs__msg__LabelInfo__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
vision_msgs__msg__LabelInfo__Sequence__are_equal(const vision_msgs__msg__LabelInfo__Sequence * lhs, const vision_msgs__msg__LabelInfo__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!vision_msgs__msg__LabelInfo__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
vision_msgs__msg__LabelInfo__Sequence__copy(
  const vision_msgs__msg__LabelInfo__Sequence * input,
  vision_msgs__msg__LabelInfo__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(vision_msgs__msg__LabelInfo);
    vision_msgs__msg__LabelInfo * data =
      (vision_msgs__msg__LabelInfo *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!vision_msgs__msg__LabelInfo__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          vision_msgs__msg__LabelInfo__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!vision_msgs__msg__LabelInfo__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
