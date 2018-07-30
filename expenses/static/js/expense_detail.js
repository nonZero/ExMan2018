// console.log("START");

$("#add-note").click(function () {
	const data = {
		content: $("#id_content").val(),
	};
	// console.log("Sending", data);
	$.post('', data, function (resp) {
		// console.log("...Got:", resp);
		$("#add-note").prop('disabled', false);
		const el = $(resp.trim());
		$("#note-form").after(el);
		el.hide().show(800);
		$("#id_content").val('').focus();
	});
	// console.log("... Sent....");
	$("#add-note").prop('disabled', true);
	return false;
});

// console.log("END");

