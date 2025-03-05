function stolenLunch(note) {
    let note = note.split("")
    note.map(c => {
      c = isNaN(c) ? String.fromCharCode((parseInt(c)+96)) : c
    })
    return note
  }