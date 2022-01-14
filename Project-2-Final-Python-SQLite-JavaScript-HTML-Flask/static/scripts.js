function CreateContent() {
  a_var = document.getElementById('my_var_a').value;
  b_var = document.getElementById('my_var_b').value;
  c_var = Math.pow(Number(a_var),2) + Math.pow(Number(b_var),2);
  document.getElementById('ContentCalc').innerHTML = Math.sqrt(c_var);
}