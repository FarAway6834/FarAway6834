function nullexcepted(func) {
	return function (value) {
		if (value === undefined) return;
		if (value === null) return;
		return func(value);
	};
}

function falsyexcepted(func) {
	return function (value) {
		if (value === undefined) return;
		if (value) return func(value);
		return;
	};
}

const nontruthyexcepted = (f => falsyexcepted(nullexcepted(f)));

const nontruthyexceptedJSONstringify = nontruthyexcepted(JSON.stringify);

const nullexceptedTrutycheck = nullexcepted(v => !!v);

class AutoComplete extends HTMLElement {
	#observer = null;
	#inputElement = null;
	#dataclassElement = null;
	#inputObserver = null;
	#datalistObserver = null;
	#idofit = null;
	#inputID = null;
	#datalistID = null;
	#inputObservingConf = {attribute: true, attributeFilter: ['id', 'list']};
	#datalistObservingConf = {attribute: true, attibuteFilter: ['id']};
	
	connectedCallback() {
		const id = this.getAttribute('id');
		this.#idofit = id;
		
		this.#inputID = `${id}-data-input`;
		this.#datalistID = `${id}-data-list`;
		
		this.#updateTags();

		this.#observer = new MutationObserver(this.#updateTags);
		this.#observer.observe(this, {childList: true});
	}

	disconnectedCallback() {
		if (this.#observer) {
			this.#observer.disconnect();
		}
		if (this.#inputObserver) {
			this.#inputObserver.disconnect();
		}
		if (this.#datalistObserver) {
			this.#datalistObserver.disconnect();
		}
	}

	#updateTags() {
		['input', 'datalist'].forEach(name => {
			const tags = Array.from(this.querySelecterAll(name));

			if (tags.length > 1) {
				console.warn(`<<auto-complete> single-child-enforer>: only one <${name}> are allowed.`);
				tags.slice(1).forEach(rmtarget => rmtarget.remove());
			}

			switch (name) {
				case "input":
					if (tags[0]) {
						const tag = tags[0];
						tag.id = tag.id || this.#inputID;
						tag.list = tag.list || this.#datalistID;
					} else {
						const tag = Object.assign(document.createElement('input'), {id : this.#inputID, type : text, class : this.#datalistID});
					}
					this.#inputElement = tag
					if (this.#inputObserver) this.#inputObserver.disconnect();
					this.#inputObserver = new MutationObserver(this.#inputObserve);
					this.#inputObserver.observe(tag, this.#inputObservingConf);
					break;
				case "datalist":
					if (tags[0]) {
						const tag = tags[0];
						tag.id = tag.id || this.#datallistID;
					} else {
						const tag = Object.assign(document.createElement('datalist'), {id : this.#datalistID});
					}
					this.#datalistElement = tag;
					if (this.#datalistObserver) this.#datalistObserver.disconnect();
					this.#datalistObserver = new MutationObserver(this.#datalistObserve);
					this.#datalistObserver.observe(tag, this.#datalistObservingConf);
					break;
				default:
					throw Error("array object for that's forEach method in <<auto-complete> single-child-enforcer> also the only logic is broken. also my mental-helth is broken too. nahhhhhhhhhhhhhhhhhhhhhh whyyyyyyyyyyy")
					break;
			}
		});
	}
	
	#inputObserve(mutation) {
		const [tag, id, list, observer, conf] = [this.#inputElement, this.#inputID, this.#datalistID, this.#inputObserver, this.#inputObservingConfig]
		if (mutation.attributeName === "id" && tag.id !== id) {
			observer.disconnect();
			tag.id = id;
			observer.observe(tag, conf);
		}
		if (mutation.attributeName === "list" && tag.list !== list) {
			observer.disconnect();
			tag.list = list;
			observer.observe(tag, conf);
		}
	}
	
	#datalistObserve() {
		const [tag, id, observer, conf] = [this.#datalistElement, this.#datalistID, this.#datalistObserver, this.#datalistObservingConfig]
		if (mutation.attributeName === "id" && tag.id !== id) {
			observer.disconnect();
			tag.id = id;
			observer.observe(tag, conf);
		}
	};
	
	normalizedDefaultList() {
		const defaultlist = this.defaultlist;
		if (!defaultlist) return;
		
		const json_parse = (json => JSON.parse(json, (k, v) => {
			switch (k) {
				case "disabled": return nullexceptedTruthcheck(v);
				case "selected": return nullexceptedTruthcheck(v);
				case "label": return nontruthyexceptedJSONstringify(v);
				case "value": return nontruthyexceptedJSONstringify(v);
				case "text": return nontruthyexceptedJSONstringify(v);
				case "":
					if (Array.isArray(v)) return v;
					return [v];
				default: return v;
			}
		}));

		const objectize = (v => {
			const typ = typeof v;
			switch (typ) {
				case "object":
					if (v === null) return {text: ""};
					if (!Array.isArray(v)) return v;
					//pass;
				case "string":
					return {text: v};
				case "boolean":
				case "number":
					if (typ === "number") v = !!v;
					return {disabled: v};
				case "undefined":
					return;
				default:
					throw new Error("whie defaultlist json normalize parsing of <auto-complete>, unjsonic type is detected. and also my broken mental health is also detected.");
					break;
			}

		json_parse(defaultlist).map(objectize).filter(x => (x !== undefined));
	}
	
	get defaultlist() {
		const ret = this.getAttribute('default-list');
		if (ret) return ret;
		return;
	}
	
	set defaultlist(value) {
		typ = typeof value;
		
		if (typ !== 'string') {
			throw new TypeError(`<<auto-complete> element's default-list attribute is string not {typ}`);
		}
		
		this.setAttribute('default-list', value);
	}

	get input() {
		return this.#inputElement;
	}

	get datalist() {
		return this.#dataclassElement;
	}

	set input(elem) {
		if (this.#inputElement) {
			this.#inputElement.before(elem);
		} else {
			this.appendChild(elem);
		}
	}
	
	set datalist(elem) {
		if (this.#dataclassElement) {
			this.#dataclasElement.before(elem);
		} else {
			this.appendChild(elem);
		}
	}
}
