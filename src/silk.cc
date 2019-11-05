#include <assert.h>
#include <node_api.h>
#include <stdio.h>
#include "Decoder.h"
#include "Encoder.h"

napi_value Decode(napi_env env, napi_callback_info info) {
  napi_status status;

  size_t argc = 2;
  napi_value args[2];
  status = napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
  assert(status == napi_ok);

  if (argc < 2) {
    napi_throw_type_error(env, nullptr, "Wrong number of arguments");
    return nullptr;
  }

  napi_valuetype valuetype0;
  status = napi_typeof(env, args[0], &valuetype0);
  assert(status == napi_ok);

  napi_valuetype valuetype1;
  status = napi_typeof(env, args[1], &valuetype1);
  assert(status == napi_ok);

  if (valuetype0 != napi_string || valuetype1 != napi_string) {
    napi_throw_type_error(env, nullptr, "Wrong arguments");
    return nullptr;
  }

  char value0[1024];
  size_t v1;
  status = napi_get_value_string_utf8(env, args[0], value0, 1024, &v1);
  assert(status == napi_ok);

  char value2[1024];
  size_t v2;
  status = napi_get_value_string_utf8(env, args[1], value2, 1024, &v2);
  assert(status == napi_ok);

  // double value1;
  // status = napi_get_value_string_utf8(env, args[1], &value1);
  // assert(status == napi_ok);

  int code = decode(value0, value2);
  napi_value ret;
  status = napi_create_int32(env, code, &ret);
  assert(status == napi_ok);

  return ret;
}

napi_value Encode(napi_env env, napi_callback_info info) {
  napi_status status;

  size_t argc = 2;
  napi_value args[2];
  status = napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
  assert(status == napi_ok);

  if (argc < 2) {
    napi_throw_type_error(env, nullptr, "Wrong number of arguments");
    return nullptr;
  }

  napi_valuetype valuetype0;
  status = napi_typeof(env, args[0], &valuetype0);
  assert(status == napi_ok);

  napi_valuetype valuetype1;
  status = napi_typeof(env, args[1], &valuetype1);
  assert(status == napi_ok);

  if (valuetype0 != napi_string || valuetype1 != napi_string) {
    napi_throw_type_error(env, nullptr, "Wrong arguments");
    return nullptr;
  }

  char value0[1024];
  size_t v1;
  status = napi_get_value_string_utf8(env, args[0], value0, 1024, &v1);
  assert(status == napi_ok);

  char value2[1024];
  size_t v2;
  status = napi_get_value_string_utf8(env, args[1], value2, 1024, &v2);
  assert(status == napi_ok);

  // double value1;
  // status = napi_get_value_string_utf8(env, args[1], &value1);
  // assert(status == napi_ok);

  int code = encode(value0, value2);

  napi_value ret;
  status = napi_create_int32(env, code, &ret);
  assert(status == napi_ok);

  return ret;
}

#define DECLARE_NAPI_METHOD(name, func)                                        \
  { name, 0, func, 0, 0, 0, napi_default, 0 }

napi_value Init(napi_env env, napi_value exports) {
  napi_status status;
  napi_property_descriptor desc[] = {
      DECLARE_NAPI_METHOD("decode", Decode),
      DECLARE_NAPI_METHOD("encode", Encode),
  };
  status =
      napi_define_properties(env, exports, sizeof(desc) / sizeof(*desc), desc);
  assert(status == napi_ok);
  return exports;
}

NAPI_MODULE(NODE_GYP_MODULE_NAME, Init)
