export default class Currency {
  constructor(code, name) {
    if (typeof code !== 'string') {
      throw TypeError('code muse be a string');
    }
    if (typeof name !== 'string') {
      throw TypeError('name muse be a string');
    }
    this._code = code;
    this._name = name;
  }

  get code() {
    return this._code;
  }

  set code(value) {
    if (typeof value !== 'string') {
      throw TypeError('code muse be a string');
    }
    this._code = value;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof value !== 'string') {
      throw TypeError('name muse be a string');
    }
    this._name = value;
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
