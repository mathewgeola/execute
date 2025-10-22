from execute import execute_javascript_by_execjs, execute_javascript_by_py_mini_racer, execute_javascript_by_subprocess


def test_execute_javascript():
    # language=javascript
    js_code = """
              function sdk () {
                let sum = 0;
                for (const n of arguments) {
                  if (typeof n === "number") sum += n;
                }
                return sum;
              }
              """
    result = execute_javascript_by_execjs(js_code, func_name="sdk", func_args=(1, 2, "3"))
    print(result)
    result = execute_javascript_by_py_mini_racer(js_code, func_name="sdk", func_args=(1, 2, "3"))
    print(result)

    # language=javascript
    js_code = """(function () {
      arguments = process.argv.slice(1).map(JSON.parse);
      let sum = 0;
      for (const n of arguments) {
        if (typeof n === "number") sum += n;
      }
      console.log(JSON.stringify({ "sum": sum }));
    })();"""

    result = execute_javascript_by_subprocess(js_code, arguments=(1, 2, "3",))
    print(result["sum"])


if __name__ == '__main__':
    test_execute_javascript()
